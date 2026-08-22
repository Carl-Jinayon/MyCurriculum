# MISTAKE LOG

> Purpose: capture mental-model errors — things the learner believed that were wrong.
> NOT for typos or trivial slips. Focus on errors that reveal a wrong mental model,
> because fixing the model prevents the entire class of error.
>
> Format per entry:
> - What the learner believed
> - What is actually true
> - Why the reasoning failed
> - Correct mental model
> - Example
> - How to recognize it next time

---

## Entry template

### 1. What the learner believed
(their words or claim)

### 2. What is actually true
(correct fact)

### 3. Why the reasoning failed
(what reasoning error produced the belief)

### 4. Correct mental model
(replacement model that prevents the error)

### 5. Example
(concrete case that exposed it)

### 6. How to recognize it next time
(trigger phrase or check)

---

## Log (most recent first)

### Entry 3 — Return value of mutating methods (2026-08-22, Day 6 mastery check)
1. **What the learner believed/wrote:** "`list.sort()` returns the original list but modified."
2. **What is actually true:** `.sort()` returns `None`; it sorts the list in place. `sorted(list)` returns a NEW sorted list.
3. **Why the reasoning failed:** knew the behavior mentally but articulated the return semantics loosely — wrote "returns" when the method only mutates.
4. **Correct mental model:** mutating methods (append, extend, insert, remove, sort, reverse) return None; value-returning methods (pop, index, count, copy) give something back. Never write `x = lst.sort()`.
5. **Example:** `b = a.sort()` makes `b` equal `None`, not the sorted list.
6. **How to recognize next time:** before assigning a method's result, ask "does this method mutate or produce?" Mutators chain to nothing.

### Entry 2 — Loop counter off-by-one (2026-08-20, Day 4 guess_game)
1. **What the learner believed:** `attempts += 1` placed after the win-check/break still counts the winning attempt.
2. **What is actually true:** code after a `break` never runs — the final attempt was never counted ("Correct! Attempts: 0" on a first-try win).
3. **Why the reasoning failed:** mentally executed the increment as if it happened every iteration, without tracing the break's exit point.
4. **Correct mental model:** trace the loop exit paths FIRST — anything after `break`/`return` is dead for that iteration.
5. **Example:** seeded test proved "82" correct on first valid guess printed Attempts: 0.
6. **How to recognize next time:** any counter/update near a `break`/`continue`/`return` → ask "does this line run on EVERY path I care about?"

### Entry 1 — Conditional fall-through in login_sim (2026-08-19, Day 3)
1. **What the learner believed:** two separate `if` blocks act like an if/elif chain — the warning would stop the program.
2. **What is actually true:** separate `if`s are independent; after printing the empty-input warning, execution continued into the credential check and ALSO printed "Access denied."
3. **Why the reasoning failed:** conflated "I handled this case" with "the program stopped here"; didn't model sequential execution through independent branches.
4. **Correct mental model:** exactly one branch of an if/elif/else chain runs; separate if-statements ALL get evaluated in order. Use elif when cases are mutually exclusive.
5. **Example:** empty inputs produced BOTH "Please enter username or password." AND "Access denied."
6. **How to recognize next time:** if two messages print where one was intended → check whether the second block should be `elif`, or use early structure so only one path executes.