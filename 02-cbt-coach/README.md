---

## C2) Project 02 — CBT Self-Help Coach (with tiny Rasa sample)  
**File:** `02-cbt-coach/README.md`
```md
# CBT Self-Help Coach

## Overview
Between-session coach that guides a brief CBT thought record: identify situation → automatic thought → evidence for/against → balanced reframe → tiny action.

## Rationale
People often forget or avoid CBT homework. A gentle, guided chat lowers effort and builds skill use.

## Flow Diagram
```mermaid
sequenceDiagram
  participant U as User
  participant B as Bot
  B->>U: Would you like a quick 5-minute CBT exercise?
  U->>B: Yes
  B->>U: What happened? (situation)
  U->>B: My manager criticized my work.
  B->>U: What thought popped up?
  U->>B: I'm terrible at my job.
  B->>U: Evidence supporting that?
  U->>B: I missed a deadline.
  B->>U: Evidence against it?
  U->>B: My last review was strong.
  B->>U: Balanced thought suggestion...
  U->>B: That feels closer to the truth.
  B->>U: Tiny action for today?
