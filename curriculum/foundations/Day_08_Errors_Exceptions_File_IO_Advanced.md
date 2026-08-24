# Day 8 Advanced — Exceptions, File I/O, and Robust Systems

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### Exception Groups (Python 3.11+)
```python
try:
    risky()
except* ValueError as eg:
    for e in eg.exceptions:
        handle(e)
except* (TypeError, KeyError) as eg:
    for e in eg.exceptions:
        handle(e)
```
`except*` catches multiple exceptions of the same group simultaneously — useful for concurrent code (asyncio, threading).

### Context Manager Protocol (build your own)
```python
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.3f}s")
        return False  # propagate exceptions

with Timer() as t:
    heavy_computation()
print(f"Took {t.elapsed:.3f}s")
```

### Context Managers with `contextlib`
```python
from contextlib import contextmanager

@contextmanager
def open_safe(path, mode="r", encoding="utf-8"):
    try:
        f = open(path, mode, encoding=encoding)
        yield f
    finally:
        f.close()

# Usage:
with open_safe("file.txt") as f:
    data = f.read()
```

### Exception Best Practices (from production systems)

**1. Never catch what you can't handle**
```python
# BAD
try:
    process()
except:
    pass

# GOOD
try:
    process()
except (ValueError, TypeError) as e:
    logger.warning(f"Bad input: {e}")
    raise
```

**2. Catch at the right level**
```python
# Low level: catch specific, convert to domain exception
def read_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise ConfigNotFoundError(path)
    except json.JSONDecodeError as e:
        raise ConfigParseError(path) from e

# High level: catch domain exceptions, decide what to do
def main():
    try:
        config = read_config("config.json")
    except ConfigNotFoundError:
        config = load_defaults()
    except ConfigParseError:
        logger.error("Corrupt config")
        sys.exit(1)
```

**3. Preserve tracebacks with `raise ... from`**
```python
try:
    process()
except ValueError as e:
    raise ProcessingError("Failed") from e  # preserves original traceback
```

**4. Never log and re-raise without context**
```python
# BAD
except Exception as e:
    logger.error(e)
    raise

# GOOD
except Exception as e:
    logger.exception("Failed to process %s", item_id)  # includes traceback
    raise
```

### File I/O — Advanced Patterns

#### Atomic Writes (never leave partial files)
```python
import os
import tempfile

def atomic_write(path, data, mode="w", encoding="utf-8"):
    dir_path = os.path.dirname(os.path.abspath(path))
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                      dir=os.path.dirname(path),
                                      delete=False) as tmp:
        tmp.write(data)
        tmp_path = tmp.name
    os.replace(tmp_path, path)  # atomic on POSIX

# Usage
atomic_write("config.json", json.dumps(config, indent=2))
```
`os.replace` is atomic on POSIX — the file is never partially written.

#### File Locking (coordination between processes)
```python
import fcntl

with open("data.json", "r+") as f:
    fcntl.flock(f, fcntl.LOCK_EX)  # exclusive lock
    data = json.load(f)
    # modify
    f.seek(0)
    json.dump(data, f)
    f.truncate()
    fcntl.flock(f, fcntl.LOCK_UN)  # unlock
```
Works on Unix; Windows needs `msvcrt.locking` or `portalocker` library.

#### Memory-Mapped Files (large files)
```python
import mmap

with open("huge.bin", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    # treat mm like a bytearray, but backed by disk
    mm[100:110] = b"new data"
    mm.flush()
```
Avoids loading entire file into RAM.

#### Streaming Large Files (iterators)
```python
def read_chunks(file_path, chunk_size=8192):
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            yield chunk

# Process line by line without loading all
for line in open("huge.log"):
    process(line)
```

#### Line Buffering vs Full Buffering
```python
# Unbuffered (immediate writes) — good for logs
with open("log.txt", "w", buffering=1) as f:
    f.write("immediate\n")

# Default: line-buffered for terminal, block-buffered for files
```

#### Pathlib Advanced
```python
from pathlib import Path

p = Path("/home/user/data")
p.iterdir()              # iterator of Path objects
p.glob("*.txt")          # pattern matching
p.rglob("*.py")          # recursive
p.resolve()              # absolute, resolve symlinks
p.relative_to(base)      # relative path
p.with_suffix(".bak")    # change suffix
p.with_name("other.txt") # change name
p.stat()                 # stat info (size, mtime, etc.)
p.touch(exist_ok=True)   # create empty file
p.mkdir(parents=True, exist_ok=True)  # mkdir -p
p.unlink(missing_ok=True) # delete file, no error if missing
p.rmdir()                # remove empty directory
p.replace(target)        # atomic replace
```

### Advanced JSON/CSV

#### JSON Lines (newline-delimited JSON) — great for streaming
```python
# Write
with open("data.jsonl", "w") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")

# Read
with open("data.jsonl") as f:
    for line in f:
        record = json.loads(line)
```

#### CSV Dialects
```python
# Custom delimiter
csv.reader(f, delimiter="|")

# Quote handling
csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # default
csv.writer(f, quoting=csv.QUOTE_ALL)      # quote everything
csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)  # quote non-numbers
```

### Retry Patterns (resilience)

#### Exponential Backoff Decorator
```python
import time
import random
from functools import wraps

def retry(max_attempts=3, base_delay=1.0, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 0.1)
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, exceptions=(IOError, ConnectionError))
def fetch(url):
    return requests.get(url).json()
```

### Circuit Breaker (prevent cascade failures)
```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failures = 0
        self.threshold = failure_threshold
        self.timeout = timeout
        self.last_failure = None
        self.state = "closed"  # closed, open, half-open

    def call(self, func, *args, **kwargs):
        if self.state == "open":
            if time.time() - self.last_failure > self.timeout:
                self.state = "half-open"
            else:
                raise CircuitOpenError()

        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except Exception as e:
            self.on_failure()
            raise

    def on_success(self):
        self.failures = 0
        self.state = "closed"

    def on_failure(self):
        self.failures += 1
        self.last_failure = time.time()
        if self.failures >= self.threshold:
            self.state = "open"
```

### Testing with Temporary Files
```python
import tempfile

def test_process_csv():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("name,score\nCarl,95\nMaria,98\n")
        fname = f.name
    try:
        result = process_csv(fname)
        assert result == {"Carl": 95, "Maria": 98}
    finally:
        os.unlink(fname)
```

### Structured Logging (observability)
```python
import logging
import json

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            record.exc_text = self.formatException(record.exc_info)
        return json.dumps(log_entry)

logging.basicConfig(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logging.getLogger().addHandler(handler)

# Usage
logger = logging.getLogger(__name__)
logger.info("User logged in", extra={"user_id": 123})
```

## 2. Explore-It-Yourself Guide

1. **Crash dump**: deliberately raise an exception, catch it, print `traceback.format_exc()` — see the full stack.
2. **File corruption**: create a corrupted JSON file, try to load it, catch `JSONDecodeError`, inspect `e.lineno`, `e.colno`.
3. **Race condition**: two processes writing same file — use `fcntl.flock` to coordinate.
4. **Memory test**: `mmap` a 1GB file, modify random bytes, compare speed vs `read()`.
5. **Retry logic**: write a function that fails twice then succeeds; wrap with `@retry(3, (IOError,))` and verify it succeeds on 3rd try.
6. **Atomic write**: write to temp file, crash the process mid-write, verify original file untouched.

### Research rabbit holes:
- "Exception chaining in Python" — why `from` matters
- "File locking across NFS" — why it's hard
- "Structured logging" — why JSON logs beat text
- "Error handling in Go/Rust" — how other languages do it

## 3. Where This Leads Later
- **Error handling** → resilience engineering, SRE, chaos engineering
- **File I/O** → data pipelines, ETL, streaming (Kafka, Spark)
- **Context managers** → resource pools, database connections, transactions
- **JSON/CSV** → APIs, configs, data interchange, ML datasets
- **Retry/circuit breaker** → microservices resilience, distributed systems
- **Atomic writes** → database internals, consensus protocols
- **Logging/observability** → SRE, debugging production systems

---

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.