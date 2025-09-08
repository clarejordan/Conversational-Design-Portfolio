---

## 🔹 Project 5 — Psychiatry Follow-Up  
**File path:** `05-psychiatry-followup/README.md`  

```md
# Psychiatry Follow-Up & Side-Effects Tracker

## Overview
A brief, periodic check-in that helps patients track mood, sleep, adherence, and side effects. Flags concerning patterns for clinician review.

## Flow Diagram
```mermaid
flowchart TD
  A[Weekly check-in consent] --> B[Mood 0–10]
  B --> C[Sleep hours + quality]
  C --> D[Medication adherence: all • some • none]
  D --> E[Side effects: none • mild • concerning]
  E --> F{Concerning?}
  F -- Yes --> G[Provide safety info + request clinician contact]
  F -- No --> H[Summarize + thank you]
