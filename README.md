# MyCurriculum — Personal Computer Science Mastery Knowledge Base

A long-term, AI-era Computer Science mastery system. This repository is my personal knowledge base and learning journal — one curriculum, one active objective, built with real implementation and verification at every step.

## What This Is

Not a normal university curriculum, not a bootcamp. A dependency-driven, adaptive CS mastery path designed for the AI era, aiming for:

- Strong CS fundamentals (DSA, systems, math, programming)
- Real engineering ability (Git, testing, debugging, deployment)
- AI-native skills (agents, LLM systems, verification of AI output)
- Employability before graduation
- Lifelong mastery after graduation

## Repository Structure

```
curriculum/
    foundations/            # Stage 0 lessons (in progress)
    computer_science/
    software_engineering/
    mathematics/
    ai_engineering/
    machine_learning/
exercises/                  # daily practice code (day_N/)
projects/                   # portfolio projects
notes/
    curriculum_state.md     # CURRENT STATE — read first
    CONTEXT_HANDOFF.md      # AI session-restore prompt
    concepts/               # concept notes
    mistakes/               # mental-model mistake log
    reviews/                # progress reviews
```

## Lesson Format

Every substantial topic produces three files in `curriculum/`:

| File | Purpose | Required |
|---|---|---|
| `Day_N_Topic.md` | Full technical reference (incl. HARD MODE optional stretch exercises) | Yes |
| `Day_N_Topic_CheatSheet.md` | Quick recall (definitions, commands, recall questions) | Yes |
| `Day_N_Topic_Advanced.md` | Optional: advanced content + explore-it-yourself guide | Optional |

Progress is measured by demonstrated capability — running code, passing checks, explaining from memory — never by reading or AI-assisted completion alone.

## Current Progress

See [notes/curriculum_state.md](notes/curriculum_state.md) for the live state.

- Stage: 0 — Foundations
- Completed: Days 1–10 (setup → types → conditionals → loops → functions → lists → tuples/sets/dicts → errors/exceptions/file I/O → OOP Primer → Learning How to Learn), Math Days 1–3 (algebra, functions, logic/sets/combinatorics), Review Day 1
- Current objective: Project 1 Expense Tracker (v0.1–v0.3) — Stage 0 capstone; then Review Day 2 + Progress Review
- Threads active: Math (parallel, Day 3 done), weekly Communication artifact, Review cycle (every 5 lessons)

## Full Subject Map

[curriculum/MASTER_CURRICULUM.md](curriculum/MASTER_CURRICULUM.md) — every subject the curriculum tackles, Stage 0 through the open end. A map, not a prison: detailed lessons are created one at a time, dependency-driven.

## Git Conventions

- One commit per meaningful unit of work (lesson, exercise batch, project milestone)
- Commit messages describe what and why
- No generated files (`__pycache__`, editor files, secrets) — see `.gitignore`