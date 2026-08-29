# Curriculum State

Updated: 2026-08-29

> SESSION CHECKLIST (AI: verify ALL before ending any session)
> [ ] state file updated (objective, threads, completed, date)
> [ ] handoff "Where we are NOW" synced
> [ ] README progress synced
> [ ] mistake log updated if new mental-model errors
> [ ] commit reminder given (git status)
> [ ] next objective stated
> Full sweep on Review Days and on learner's "system check" command.

## Learner Profile
- 20, 3rd-year CS student, Philippines, ~2 years from graduation
- 3-5 hrs/day self-study available
- Goal: exceptional CS student before graduation; employable early; lifelong mastery

## Current Stage
- Stage 0 — Foundations (in progress)

## Current Learning Objective
- MASTERY WEEK (Stage 0 capstone) — see notes/MASTERY_WEEK.md
- M1 COMPLETE: Day 9 OOP Primer VERIFIED (2026-08-25) — classes/__init__/self/inheritance/custom exceptions w/ payloads, type-hints unprompted
- M2 COMPLETE: Day 8 errors/exceptions/file I/O VERIFIED (2026-08-28)
- M3 Day 10 COMPLETE: Learning How to Learn VERIFIED (2026-08-29). HM backlog (≥2 Hard Mode from Days 1–7, AI-free) still pending.
- M4–M5 NEXT: Project 1 Expense Tracker (v0.1–v0.3 + README + feature commits); then M6 Review Day 2 · M7 Progress Review
- Missed lessons resolved: OOP→Day 9, LHTL→Day 10, Git formal→Stage 1 Day 1

## Active Threads (in addition to main objective)
- Math thread: Math_01 + Math_02 + Math_03 VERIFIED
- Communication thread: Week 01 done; Week 02 artifact due
- Review cycle: Review Day 1 complete; Review Day 2 scheduled after Project 1 (M6)
- Domain journal: starts at first real project

## Completed Objectives
- Day 1 (2026-08-17): Python setup, first program, variables, print/input, terminal basics, debugging loop — VERIFIED
- Day 2 (2026-08-17): data types, arithmetic, strings, conversions, f-strings — VERIFIED
- Day 3 (2026-08-19): conditionals, comparisons, boolean logic, input validation — VERIFIED (classifier, even_odd_v2, grade, login_sim, validator, FizzBuzz mastery); login_sim empty-input bug found and fixed by learner
- Day 4 (2026-08-20): loops — while, for, range, break/continue/else — VERIFIED (countdown, sum_until_zero, multiplication_table, guess_game, pattern_printer, validation_retry, mastery sum 1..N + traces correct); guess_game attempts off-by-one found, learner fixed
- Day 5 (2026-08-21): functions (parameters, return, scope) — VERIFIED (my_functions, string_utils, temperature, validator_fn, calculator_fns)
- Math Day 1 (2026-08-22): algebra — VERIFIED (evaluation, simplification, one-step equations with checks, word problems, python bridge)
- Review Day 1 (2026-08-22): cumulative Days 1–5, AI-free — VERIFIED (6/6 exercises; factorial even/odd fix; README documented)
- Communication Week 01 (2026-08-22): concepts explained in own words — DONE
- Day 6 (2026-08-22): lists — VERIFIED (basics/slicing, methods incl. reverse, enumerate + accumulator stats, nested comprehension grid, aliasing demo, filter via comprehension AND loop); coaching note: avoid shadowing built-in names (max/min → maximum/minimum, fixed)
- Day 7 (2026-08-23): tuples, sets, dicts — VERIFIED (all 6 exercises: tuple basics with immutability demo, set basics with add/discard/membership, dict CRUD with safe .get/delete, inventory management, word frequency counter, contact book with safe lookup/rename); inventory total 22, most stacked = cherry, word counts correct, contact book rename logic working
- Math Day 2 (2026-08-22): functions notation/evaluation — VERIFIED (forward eval, reverse solve, Python bridge)
- Math Day 3 (2026-08-24): logic/sets/combinatorics — VERIFIED (truth tables incl. 3-var, set operations, inclusion-exclusion counting; see mistake log entry 4)
- Day 8 (2026-08-28): errors/exceptions/file I/O — VERIFIED (safe_int, PositiveIntegerError + retry loop, file_read w/ line numbers + FileNotFoundError/PermissionError, scores.csv round-trip w/ headers + average, config.json dump/load + corrupt-file handling, log_analyzer counts ERROR/WARNING/INFO w/ malformed-line tolerance)
- Day 10 (2026-08-29): Learning How to Learn — VERIFIED (forgetting_curve: 5 techniques + one place each; mistake_recall: 4 entries from memory; feynman_drill: weakest concept explained to 12-year-old no-jargon; study_protocol.py spaced-repetition JSON tool w/ bootstrap)
- Day 9 (2026-08-25): OOP Primer — classes/__init__/self/inheritance/custom exceptions w/ payloads, type-hints, validator_oop rewrite — VERIFIED (bank_account, student_class, shape_isinstance, class_vs_dict, validator_oop)

## Assessed Levels (2026-08-17)
- Programming: complete beginner
- Algebra: basically new
- Functions: no
- Terminal: never used
- Git: never used
- AI collaboration: Level 1 (asks for code/explanations)
- University: treating as zero — fresh start

## Demonstrated Competencies
- Can create a .py file and run it with python3
- Can use print(), input(), variables, basic string concatenation-free printing
- Writes prediction before running code (good habit)
- Read error messages and fixed typos (break-and-fix exercise done)
- Uses comparison operators correctly and understands if/elif/else branching
- Validates input before converting (check → convert → use pattern)
- Boolean logic: and, or, not, understands truthiness basics
- Writes FizzBuzz from memory
- Loops: while, for+range, break/continue/loop-else; nested loops; accumulator and validation-retry patterns; traces loops correctly by hand
- Debugging: found and fixed own bugs (login_sim empty-input, guess_game off-by-one) from feedback
- Defines functions with parameters, return values; understands local vs global scope; uses default parameters
- Composes programs from small functions (validator_fn, string_utils, temperature conversions)
- Lists: indexing/slicing/negative indices, core methods (append/extend/pop/remove/index/count/sort/reverse/copy), enumerate/zip awareness, nested list grids via comprehension, aliasing vs copy understood and demonstrated, filtering via both comprehension and loop
- Math: evaluates expressions with negatives, simplifies like terms, solves one-step equations WITH checking, function notation f(x) — evaluate AND reverse, connects math functions to Python def
- Tuples: immutability, unpacking, single-element syntax, indexing/slicing, when to use
- Sets: creation, deduping, add/discard/remove, membership testing, union/intersection/difference, no indexing
- Dicts: CRUD, safe access with .get(), .get() for conditional deletion, .items() iteration, nested dicts, counting pattern
- Day 8 (verified): try/except/else/finally; raises and defines custom exceptions (PositiveIntegerError); file I/O with `with`; CSV round-trip with header + DictReader/DictWriter (scores.csv average); JSON dump/load with corrupt-file + missing-file handling (config.json); log parsing/counting with malformed-line tolerance (log_analyzer.py)
- Day 9 (verified): OOP — classes, __init__, self, inheritance; custom exceptions with payloads (InsufficientFundsError/InvalidDepositAmount); type hints; validator_oop rewrite (bank_account.py, student_class.py, shape_isinstance.py, class_vs_dict.py)
- Day 10 (verified): names the five learning techniques and where the curriculum applies each; recalls all 4 mistake-log entries from memory; explains a concept Feynman-style (12-year-old, no jargon); built study_protocol.py spaced-repetition JSON tool

## Weak Areas
- No major weak areas demonstrated at Stage 0 close; learner is in consolidation/integration stage (Project 1 next)
- Residual notes: int() truncates floats rather than raising (clarified); list.sort() returns None (mutator, not producer) — both reinforced
- Upcoming risk: integrating many concepts in Project 1; spaced-repetition discipline depends on actually using study_protocol.py

## Current Projects
- None

## Mathematics Level
- Beginner (algebra/functions fresh)

## Programming Level
- Beginner

## AI Collaboration Level
- Level 1 — Basic AI Assistance

## Portfolio Status
- None

## Employability Status
- Not employable yet (expected: developing in Stage 2)

## Important Mistakes
- (Empty — no lessons completed)

## Upcoming Prerequisite Needs
- Algebra/functions (for all later math)
- Terminal basics (for all tooling)
- Python fundamentals (for DSA, web, AI)