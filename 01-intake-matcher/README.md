# Therapist Matching Intake Assistant

## Overview
A friendly, stepwise intake that replaces cold forms with a short conversation. Goal: reduce drop-off, capture preferences, and improve initial match quality.

## Problem
New clients often feel anxious filling forms. Key details get missed, leading to poor matches and reschedules.

## Flow Diagram
```mermaid
flowchart TD
  A[Hello + consent] --> B[Reason for seeking therapy]
  B --> C[Goals]
  C --> D[Preferences]
  D --> E[Modality]
  E --> F[Scheduling]
  F --> G[Insurance]
  G --> H[Confirm]
  H --> I[Match summary]
```

## Example Dialog
**Bot:** Hi, I’ll ask a few short questions to help match you with a therapist. You can skip anything. Ready?  
**User:** Yes.  
**Bot:** What brings you to therapy?  
**User:** Anxiety at work.  
**Bot:** Thanks. What would you like therapy to help with? (options)  
**User:** Reducing anxiety and sleep.  
**Bot:** Got it. Any therapist preferences?  
**User:** Someone direct and practical.  
**Bot:** Thanks. Do you prefer virtual, in-person, or either?  
**User:** Virtual.  
**Bot:** When are you usually available?  
**User:** Evenings.  
**Bot:** Will you use insurance or self-pay?  
**User:** Insurance.  
**Bot:** Great — here’s your summary. Looks good?  
**User:** Yes.  
**Bot:** Perfect. Let’s find your therapist match.
