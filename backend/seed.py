import sys

from app import create_app
from app.models import db, Task

app = create_app()

with app.app_context():
    db.create_all()

    if Task.query.first():
        print("Database already has data, skipping seed.")
        sys.exit(0)

    tasks = [
        Task(title="Buy groceries", description="Milk, eggs, bread, vegetables"),
        Task(title="Finish homework", description="Complete the math assignment"),
        Task(title="Walk the dog", description="30 minutes in the park"),
        Task(title="Read a book", description="Finish chapter 5 of 'Atomic Habits'"),
        Task(title="Call mom", description="Weekly catch-up call"),
    ]

    for task in tasks:
        db.session.add(task)

    db.session.commit()
    print(f"Seeded {len(tasks)} tasks.")
