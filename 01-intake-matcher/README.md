# Therapist Matching Intake Assistant

## Overview
A friendly, stepwise intake that replaces cold forms with a short conversation. Goal: reduce drop-off, capture key preferences, and improve initial match quality.

## Problem
New clients often feel anxious and overwhelmed by long forms. Important nuances about goals, scheduling, modality, or preferences get skipped or rushed, leading to poorer matches and rescheduling.

## Users & Goals
- **New client** wants to feel understood and get matched quickly.
- **Provider ops** wants clean, structured data to route accurately.

## Constraints
- Respect privacy, collect the minimum necessary.
- Offer “skip” or “prefer not to say” for sensitive items.
- Never give clinical advice; this is intake only.

flowchart TD
  A[Hello + consent + what to expect] --> B[Reason for seeking therapy]
  B --> C[Goals (pick or type)]
  C --> D[Preferences: therapist style; optional identity]
  D --> E[Modality: virtual / in-person / hybrid]
  E --> F[Scheduling windows + time zone]
  F --> G[Insurance or self-pay]
  G --> H[Review + edit answers]
  H --> I[Match summary + next steps]
  I --> J[Optional: first-session tips]
