# Day 10 — Learning How to Learn: The System Behind the Curriculum

## Objective
- Understand the learning science your curriculum has been silently applying
- Master five techniques: spaced repetition, active recall, deliberate practice, interleaving, the Feynman technique
- Build metacognition: distinguishing KNOWN from CLAIMED
- Leave with a personal, concrete study protocol

## Prerequisites
- Days 1–8 completed — you've been DOING these techniques; this lesson names them

## Why This Matters
You have now experienced ~10 lessons and one review cycle. Every mechanism I've used — predict-before-run, mistake log, review days, Hard Mode, mastery checks — is applied cognitive science. This lesson makes the invisible visible, because a learner who understands *why the system works* can eventually run it without me. That independence (§30 of the master plan) is the actual graduation condition.

## The Five Techniques

### 1. Spaced Repetition — fight the forgetting curve
Memory decays exponentially after learning; each well-timed review flattens the decay.
```
Review at: 1 day → 3 days → 7 days → 2 weeks → 1 month
```
**Where you already do this:** Review Day 1 re-tested everything; mistake-log entries get re-tested every cycle. **Upgrade:** your mistake log now has 4 entries — before Stage 1 starts, answer each from memory, then check.

### 2. Active Recall — retrieval IS the learning
Re-reading feels productive but builds recognition, not recall. Forcing retrieval (answering from memory, writing code blank) rebuilds and strengthens the pathway.
**Where you already do this:** every Mastery Check "from memory", FizzBuzz rewrite, cheat-sheet Active Recall questions. **Upgrade:** never re-read a lesson without first attempting its recall questions.

### 3. Deliberate Practice — train at the edge, not in comfort
Repeating what you can already do is performance, not practice. Growth happens at the boundary where success isn't guaranteed.
**Where you already do this:** Hard Mode (your principle!), break-and-fix drills, exercises that combine 2+ old concepts. **Upgrade:** when an exercise feels easy, that's the signal to add a constraint or edge case — not to skip ahead bored.

### 4. Interleaving — mix topics; force discrimination
Blocked practice (all loops, then all functions) feels smooth but teaches pattern-matching by chapter. Mixed practice forces you to ask "which tool fits HERE?" — the actual skill.
**Where you already do it:** review days, bridge.py (logic+sets+counting in one program), Project 1 upcoming. **Upgrade:** in the expense tracker, deliberately interleave: validation + files + dicts in the same session.

### 5. The Feynman Technique — explain simply or you don't know it
Write/say the explanation as if to a smart 12-year-old; gaps become instantly visible.
**Where you already do this:** communication artifacts (Week_01.txt), code comments, mastery-check explanations. **Upgrade:** every Week-N artifact = Feynman for ONE concept, no AI, then read it aloud once — your ear catches what your eye forgives.

## Metacognition — the KNOWN / CLAIMED / UNKNOWN discipline

| State | Meaning | Test |
|---|---|---|
| KNOWN | demonstrated under verification | ran it, explained it, transferred it |
| CLAIMED | feels familiar | — dangerous zone |
| UNKNOWN | honest zero | fine — schedule it |

The feeling of knowing ≠ knowing. Fluency illusion comes from re-reading and AI-generated answers. The only escape is testing yourself before checking — exactly the predict-first habit from Day 2.

## Your Personal Protocol (from now on)

Per new concept:
1. **Learn** small (main lesson)
2. **Retrieve** immediately (mastery check, no notes)
3. **Practice at the edge** (core exercises → Hard Mode)
4. **Interleave** into projects/review days
5. **Explain** (Feynman artifact or teaching moment)
6. **Space** (reappear on review days; mistakes get re-tested)
7. **Log failures** (mistake log — they're data, not shame)

With AI specifically:
- Attempt first → hint not answer → verify everything → occasionally go fully AI-free (review days) to prove the underlying ability survived

## Common Mistakes
- Re-reading/highlighting as "studying" — passive exposure is recognition theater
- Cramming before review days instead of trusting spacing
- Practicing only comfortable exercises (blocked, easy = performance not growth)
- Confusing "I've seen this" with "I can produce this"
- Skipping the reflection sections — metacognition skipped is the system half-run

## Verification Checklist
- [ ] I can name the five techniques and where my curriculum applies each
- [ ] I can explain the forgetting curve and why review days are spaced as they are
- [ ] I attempted all four mistake-log entries from memory BEFORE reading them
- [ ] I wrote this week's Feynman artifact on a concept WITHOUT AI first

## Exercises (exercises/Foundations/day_10/)
1. `forgetting_curve.txt` — From memory: list the five techniques and one place your curriculum applies each. Then check against this lesson; note what you missed.
2. `mistake_recall.md` — Answer all 4 mistake-log entries from memory (what was believed / what's true / recognize-next-time). THEN open the log and grade yourself honestly.
3. `feynman_drill.md` — Pick the concept you understand LEAST so far (loops? scope? hash tables?). Explain it in ≤150 words as if to a 12-year-old. No jargon allowed.
4. `study_protocol.py` — yes, code it: a tiny program storing {concept: last_reviewed_date} in a JSON file that prints which concepts are due today per the spacing schedule (1d, 3d, 7d, 14d). It will serve you for the rest of the curriculum — real tool, real learning.

## HARD MODE (optional)
1. Upgrade #4 with due-date sorting and an "overdue" flag.
2. Add spaced-repetition logic INTO the ledger: mark concepts reviewed; auto-promote interval.
3. Research (no code): compare spaced repetition vs massed practice evidence (Ebbinghaus, Roediger & Karpicke). One page, plain English, sources cited.

## Mastery Check (from memory)
1. Name the five techniques.
2. What is the fluency illusion and what defeats it?
3. Which technique does the mistake log implement?
4. Write your 7-step personal protocol from memory.

## Reflection
- Which technique have you been skipping?
- Where did the feeling of knowing fool you this month?
- What will YOU change about how you study tomorrow?

## Key Takeaways
- Retrieval beats re-reading; spacing beats cramming; edge beats comfort; mixing beats blocking; explaining beats recognizing
- The curriculum's mechanisms ARE these techniques — now you can run them yourself
- Metacognition (KNOWN vs CLAIMED) is the master skill underneath all five
- The endgame: you won't need me to tell you what to study