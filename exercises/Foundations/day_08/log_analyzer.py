import logging

logging.basicConfig(
    filename="data/app.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    filemode="w"
)

logging.info("server started")
logging.error("database connection failed")
logging.warning("low disk space")
logging.info("user logged in")
logging.error("timeout contacting API")
logging.warning("retry scheduled")
logging.info("shutdown complete")

counts = dict()
try:
    with open("data/app.log", "r", encoding="utf-8") as f:
        logs = f.readlines()
except FileNotFoundError:
    print("File doesn't exist.")
else:
    parse_count = 0
    for log in logs:
        if ": " not in log:
            continue
        level, message = log.split(": ", 1)
        counts[level] = counts.get(level, 0) + 1
        parse_count += 1

for level, count in counts.items():
    print(f"{level}: {count}")

print(f"Total lines parsed: {parse_count}")
