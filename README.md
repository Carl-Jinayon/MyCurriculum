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
| `Day_N_Topic.md` | Full technical reference | Yes |
| `Day_N_Topic_CheatSheet.md` | Quick recall (definitions, commands, recall questions) | Yes |
| `Day_N_Topic_Advanced.md` | Optional: advanced content + explore-it-yourself guide | Optional |

Progress is measured by demonstrated capability — running code, passing checks, explaining from memory — never by reading or AI-assisted completion alone.

## Current Progress

See [notes/curriculum_state.md](notes/curriculum_state.md) for the live state.

- Stage: 0 — Foundations
- Completed: Day 1 (Python setup, first program, variables, print/input, terminal, debugging)
- Current objective: Day 2 (data types, arithmetic, strings)

## Git Conventions

- One commit per meaningful unit of work (lesson, exercise batch, project milestone)
- Commit messages describe what and why
- No generated files (`__pycache__`, editor files, secrets) — see `.gitignore`