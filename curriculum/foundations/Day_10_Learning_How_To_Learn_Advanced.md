# Day 10 Advanced — The Learning Science, Deeper

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### The evidence base (know why, not just what)
- **Ebbinghaus (1885)** — forgetting curve: retention decays roughly exponentially; relearning is faster each time (savings effect)
- **Roediger & Karpicke (2006)** — testing effect: retrieval practice beat repeated study by huge margins at 1-week delay
- **Bjork — desirable difficulties**: conditions that slow acquisition (spacing, interleaving, generation) improve long-term retention; ease during practice ≠ learning
- **Ericsson — deliberate practice**: expert performance = focused practice on specific sub-skills at the edge of ability + immediate feedback; NOT hours of comfortable repetition
- **Dunlosky et al. (2013)** — meta-review ranking techniques: practice testing and distributed practice = HIGH utility; highlighting/rereading/summarizing = LOW

### Generation effect & errorful learning
Generating an answer (even wrong) before seeing the correct one improves later retention versus passive reading. This is WHY the curriculum demands predictions before running code and forbids answer-first AI usage. Being wrong then corrected beats being told.

### Desirable difficulty calibration
Difficulty must be *desirable* — achievable with effort:
```
comfort zone    → no growth (performance theater)
desirable zone  → struggle + eventual success (growth)
impossible zone → frustration, copying, fake mastery
```
Calibration signal: you know what's wrong and can hypothesize (desirable) vs you cannot even start (move back one prerequisite).

### Metacognition research
- **Dunning-Kruger effect**: low skill inflates self-assessment — beginners most at risk of "I know this"
- **Judgment of Learning (JOL)**: learners' predictions are unreliable UNLESS based on a retrieval attempt — hence mastery checks BEFORE advancing, never confidence surveys
- **Illusion of competence from worked examples**: watching solutions creates familiarity that mimics knowledge; AI-generated code supercharges this illusion — which is why AI-free checkpoints exist in your curriculum

### Motivation science (the part nobody teaches)
- **Self-Determination Theory**: sustained motivation requires autonomy (you chose this), competence (visible progress — your ledger/state files), relatedness (community — GitHub presence)
- **Goal gradients**: progress toward completion accelerates effort — visible stage progression exploits this honestly
- **Identity-based habits** ("I am someone who verifies before claiming") outlast outcome-based goals ("finish X lessons")

### Spaced repetition scheduling theory
- Expanding intervals (1→3→7→14d) approximate optimal recall success ~90%
- Failure resets the interval (that's why mistake-log failures restart spacing)
- Modern algorithms (SM-2/FSRS in Anki) compute per-item difficulty — your study_protocol.py Hard Mode builds a baby version

### Transfer — the truest test of learning
Near transfer: same domain new problem (loops → different loop). Far transfer: different domain (loop discipline → ML training epochs mindset). Far transfer rarely happens automatically — it requires deliberate abstraction ("what's the general pattern here?"). The Reflection sections exist to force abstraction questions.

## 2. Explore-It-Yourself Guide

1. Self-experiment: pick two similar concepts (e.g., // vs %). Learn one by rereading, one by retrieval quizzing. Test both after 3 days. Feel the difference yourself.
2. Audit your last week against Dunlosky's rankings — how many hours went to HIGH-utility vs LOW-utility activities?
3. Feynman audit: take your Week_01 artifact; mark every sentence containing jargon you can't define without docs.
4. Design experiment: predict which Day-8 exercise will feel hardest in 2 weeks; schedule its review; check your prediction accuracy (calibration training).
5. Read one primary source (Roediger & Karpicke 2006 abstract is readable) — experience learning from papers before Stage 1 forces it.

## 3. Where This Leads Later
- These skills compound into Stage 1+ where material density triples — the system matters more as content accelerates
- Deliberate practice framework → interview prep, competitive programming
- Metacognition → debugging your own understanding, code review of self
- Teaching (Feynman) → open-source contributions, blog posts, mentoring — employability multipliers

## Final Rule
Optional files never gate your progress. But if any Advanced file deserves full reading, it is this one.