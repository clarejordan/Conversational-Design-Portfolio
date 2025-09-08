---

## C3) Project 03 — DBT Distress De-escalation  
**File:** `03-dbt-distress/README.md`
```md
# DBT Distress De-escalation (TIPP + Grounding)

## Overview
Rapid skills flow to reduce acute emotional arousal using DBT techniques (TIPP) and grounding. Clear off-ramps to crisis resources when needed.

## Flow Diagram
```mermaid
flowchart TD
  A[Check safety keywords] -->|crisis detected| ESC[Escalate using safety snippet]
  A -->|no crisis| B[Name emotion + intensity 0–10]
  B --> C[Choose skill: paced breathing, cold water, grounding, opposite action]
  C --> D[Guide 60–90 seconds]
  D --> E[Re-rate intensity]
  E --> F{Down by ≥2?}
  F -- Yes --> G[Reinforce + tiny plan]
  F -- No --> H[Try a second skill or suggest human support]
