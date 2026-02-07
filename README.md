# Task Acceptance & Slot Logic API

This project implements Task 8 from the internship assignment.
I focused on backend validation to prevent over-acceptance of tasks with limited slots.

## Tech Stack
- Python
- Flask

## API Endpoint
POST /tasks/<task_id>/accept

## Logic
- Check if the task exists
- Validate available slots
- Reduce slot count on acceptance
- Block acceptance when slots reach zero

This ensures data integrity in task-based systems.

## Running the Project
```bash
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py
