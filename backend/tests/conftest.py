import pytest
from app import create_app
from app.models import db, Task


@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def sample_task(app):
    with app.app_context():
        task = Task(
            title="Test Task",
            description="A test task description",
        )
        db.session.add(task)
        db.session.commit()
        task_id = task.id
    return task_id


@pytest.fixture
def sample_tasks(app):
    with app.app_context():
        tasks = [
            Task(title="First Task", description="First description"),
            Task(title="Second Task", description="Second description"),
            Task(title="Third Task", description="Third description"),
        ]
        db.session.add_all(tasks)
        db.session.commit()
        task_ids = [t.id for t in tasks]
    return task_ids
