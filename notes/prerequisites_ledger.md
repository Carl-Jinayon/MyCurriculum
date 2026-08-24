# PREREQUISITES LEDGER — Core-Exercise Dependency Matrix

> Purpose: every construct REQUIRED by a CORE exercise must be taught in a PRIOR MAIN lesson
> (Exercise Dependency Rule). This ledger maps required constructs to where they are taught.
> "ADV" = satisfied by an Advanced file + explicit pointer in exercise text (weaker guarantee).
> Audit origin: 2026-08-24 — gaps #1 modules/imports, #2 split(), #3 padding, #4 comments,
> #5 docstrings, #6 None, #7 chained comparisons found and resolved.

| Exercise | Required construct | Taught in | Status |
|---|---|---|---|
| day_01 greet/hello/variables | print, input, variables, str/int | Day 1 main | ✅ |
| day_01 HM receipt | padding/alignment; string repetition `*` | Day 1 ADV (padding) / Day 2 main (`*`) | ✅ pointer |
| day_02 all | f-strings, arithmetic, //, %, **, conversions | Day 2 main | ✅ |
| day_02 type_check | type() | Day 2 main | ✅ |
| day_03 classifier | startswith() [learner-initiated] | Day 3 ADV (string methods) | ✅ ADV |
| day_04 guess_game | import random, randint | **Day 4 main anchor** + Day 4 ADV full | ✅ fixed |
| day_05 validator_fn | while-loop validation | Day 4 main | ✅ |
| day_06 filter_list | list comprehension | Day 6 main | ✅ |
| day_07 word_freq | str.split(), dict.get pattern | **Day 2 main anchor** (split) + Day 2 ADV table; counting pattern Day 7 main | ✅ fixed |
| day_07 contact_book | dict CRUD, .get(), del | Day 7 main | ✅ |
| day_08 exceptions_* | try/except/raise/custom classes* | Day 8 main (*classes formally Stage 1; minimal pattern shown in Day 8 main) | ✅ |
| day_08 json_config/csv | import json/csv/pathlib | **Day 8 main** (import anchor) + Day 8 ADV deep | ✅ |
| math_03 bridge.py | functions-as-values, itertools.product [lesson-suggested], lambda [learner-initiated] | Day 5 ADV (higher-order); product named in exercise text | ✅ |

## Known learner-initiated constructs (not yet formally taught — acceptable)
- lambda expressions (math_03) → formal treatment: Stage 1
- abs() (math_03 sets) → note added in Math Day 3 feedback
- chained comparisons (day_04 validation_retry) → Day 3 main anchor added

## Rule for future lessons
Before writing a core exercise: list its required constructs; each must appear in a PRIOR
main lesson OR get an explicit pointer + ADV coverage. Append the row here.