# Task Acceptance & Slot Logic API

This project implements the Task Acceptance & Slot Logic as part of an internship assignment.
The goal is to ensure that tasks with limited slots cannot be over-accepted.

---

## Tech Stack
- Python
- Flask
- In-memory data storage

---

## Problem Statement
Each task has a limited number of available slots.
A user can accept a task only if slots are available.
Once slots reach zero, further acceptance is blocked.

---

## API Endpoint

### Accept Task
POST /tasks/<task_id>/accept

#### Success Response
```json
{
  "message": "Task accepted successfully",
  "remaining_slots": 1
}
