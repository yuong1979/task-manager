from datetime import datetime
from app.models import db, Task


class TestTaskModel:
    def test_create_task(self, app):
        with app.app_context():
            task = Task(
                title="My Task",
                description="My description",
            )
            db.session.add(task)
            db.session.commit()

            assert task.id is not None
            assert task.title == "My Task"
            assert task.description == "My description"
            assert task.completed is False
            assert isinstance(task.created_at, datetime)
            assert isinstance(task.updated_at, datetime)

    def test_task_default_completed(self, app):
        with app.app_context():
            task = Task(title="Default Check")
            db.session.add(task)
            db.session.commit()

            assert task.completed is False

    def test_task_nullable_description(self, app):
        with app.app_context():
            task = Task(title="No Desc")
            db.session.add(task)
            db.session.commit()

            assert task.description is None

    def test_task_to_dict(self, app):
        with app.app_context():
            task = Task(
                title="Dict Task",
                description="Dict desc",
                completed=True,
            )
            db.session.add(task)
            db.session.commit()

            d = task.to_dict()
            assert d["id"] == task.id
            assert d["title"] == "Dict Task"
            assert d["description"] == "Dict desc"
            assert d["completed"] is True
            assert d["created_at"] == task.created_at.isoformat()
            assert d["updated_at"] == task.updated_at.isoformat()

    def test_task_updated_on_modify(self, app):
        with app.app_context():
            task = Task(title="Update Me")
            db.session.add(task)
            db.session.commit()

            original_updated = task.updated_at
            task.title = "Updated Title"
            db.session.commit()

            assert task.updated_at > original_updated
