# LifePilot - Full Project Specification

---

# 1. Overview

## Executive Summary

LifePilot is a conversational personal assistant designed for people with ADHD (TDA). It unifies expense tracking, task management, and habit building into a simple chat-driven workflow.

Instead of traditional apps with forms and lists, LifePilot allows users to send short messages that are automatically transformed into structured actions.

---

## Problem

Users with ADHD struggle with:
- Capturing information quickly
- Organizing tasks and finances
- Maintaining priorities

This leads to:
- Lost expenses
- Accumulated tasks
- Cognitive overload

---

## Solution

A conversational system that:
- Converts messages into structured data
- Automatically prioritizes daily actions
- Generates summaries and feedback

---

## Target Users

- Adults with ADHD (25–45)
    
- Freelancers / independent professionals
    
- Users seeking simplicity over complex tools
    

---

## Value Proposition

"Your life organized through simple messages. No infinite lists, only what matters today."

---

# 2. Product Features

## MVP Features

- Chat-based input
    
- Daily dashboard
    
- Weekly summaries
    
- Basic categorization (rule-based)
    
- Habit tracking (streaks)
    

## Future Features

- Push notifications
    
- Calendar & banking integrations
    
- Predictive insights (AI)
    
- Multi-user support
    

---

# 3. System Architecture

## High-Level Architecture

```
[Telegram Bot]
      ↓
[Webhook - Spring Boot]
      ↓
[Core API]
      ↓
[PostgreSQL (Supabase)]
      ↓
[SvelteKit Dashboard]
```

## Key Decisions

- Use Spring Events for internal communication
    
- Telegram is primary interface
    

---

# 4. Tech Stack

## Backend

- Spring Boot 3 (Java 21)
- Gradle
- Spring Data JPA    

## Database

- PostgreSQL (Supabase as hosting only)

## Frontend

- SvelteKit
- Cloudflare Pages

## Auth

- Telegram ID as primary identity
- JWT optional

## DevOps

- Docker
- Render (backend)
- GitHub Actions

## Testing

- JUnit 5
    
- Testcontainers (Postgres only)
    

---

# 5. Data Model

## expenses

- id
    
- amount
    
- category
    
- date
    
- note
    
- source
    
- confidence
    

## tasks

- id
    
- description
    
- due_date
    
- status
    
- priority
    

## habits

- id
    
- name
    
- streak
    
- last_completed
    

## users

- id
    
- telegram_id
    
- preferences
    

---

# 6. Message Parser Design

## Objective

Convert unstructured user messages into structured actions.

---

## Strategy

### Layer 1: Preprocessing

- Normalize text (lowercase, trim)
    
- Replace commas with dots in numbers
    
- Remove extra spaces
    

---

### Layer 2: Intent Detection

Detect intent using rule-based classification:

- Expense → contains number + keyword (€, $, etc.)
    
- Task → contains verbs like "pagar", "hacer"
    
- Habit → keywords like "gym", "leer"
    

---

### Layer 3: Entity Extraction

#### Expense Example

Input:  
"café 3,20"

Output:

```
{
  type: "expense",
  amount: 3.20,
  category: "food",
  note: "café"
}
```

#### Task Example

Input:  
"pagar alquiler viernes"

Output:

```
{
  type: "task",
  description: "pagar alquiler",
  due_date: "next friday"
}
```

---

### Layer 4: Rule Engine

- Regex for amounts: `\\d+[.,]?\\d*`
    
- Date parsing: keywords (hoy, mañana, viernes)
    
- Category mapping:
    
    - café → food
        
    - uber → transport
        

---

### Layer 5: Confidence Score

Each parse includes a confidence score (0–1):

- High: clear patterns
    
- Medium: partial match
    
- Low: fallback
    

---

### Layer 6: Fallback Handling

If confidence < threshold:

- Store as "unclassified"
    
- Ask user for clarification
    

---

## Future Enhancement

- Add lightweight AI (LLM or embeddings)
    
- Hybrid system: rules + AI
    

---

# 7. API Design

## Base URL

```
/api
```

---

## Telegram

### POST /telegram/webhook

Receives user messages

Request:

```
{
  message: "café 3,20",
  telegram_id: "123456"
}
```

Response:

```
{
  status: "processed"
}
```

---

## Dashboard

### GET /dashboard/today

Returns prioritized daily items

Response:

```
{
  tasks: [],
  expenses: [],
  habits: []
}
```

---

## Finances

### GET /finances/week

Weekly summary

---

## Habits

### GET /habits/progress

Returns streaks and completion data

---

## Tasks

### GET /tasks

### POST /tasks

### PATCH /tasks/{id}

---

## Expenses

### GET /expenses

### POST /expenses

---

## Health

### GET /health

---

# 8. Internal Flow

1. User sends message via Telegram
    
2. Webhook receives message
    
3. Parser processes input
    
4. Data stored in Postgres
    
5. Spring Event triggered
    
6. Dashboard reflects changes
    

---

# 9. Roadmap

## Week 1

- Telegram webhook
    
- Expense parsing
    
- DB persistence
    

## Week 2

- Tasks
    
- Dashboard
    

## Week 3

- Habits
    
- Weekly summaries
    

## Week 4

- Auth (optional)
    
- Testing
    
- Deployment
    

---

# 10. Deployment

## Backend

- Docker image
    
- Deploy to Render
    

## Frontend

- Deploy to Cloudflare Pages
    

---

# 11. Future Improvements

- AI parsing
    
- Notifications
    
- Realtime updates
    
- Multi-user system
    

---

# 12. Required Skills

- Backend Engineering (Spring Boot)
    
- System Design
    
- Conversational UX
    
- Frontend (SvelteKit)
    
- DevOps (Docker, CI/CD)
    

---
*End of Document*