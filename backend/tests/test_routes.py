import json


class TestTaskRoutes:
    def test_list_tasks_empty(self, client):
        resp = client.get("/api/tasks")
        assert resp.status_code == 200
        assert resp.get_json() == []

    def test_list_tasks_with_data(self, client, sample_tasks):
        resp = client.get("/api/tasks")
        assert resp.status_code == 200
        data = resp.get_json()
        assert len(data) == 3
        titles = [t["title"] for t in data]
        assert "Third Task" in titles
        assert "Second Task" in titles
        assert "First Task" in titles

    def test_list_tasks_ordered_by_newest(self, client, app):
        with app.app_context():
            from app.models import Task, db

            task = Task(title="Old Task")
            db.session.add(task)
            db.session.commit()
            old = db.session.get(Task, task.id)
            old.created_at = old.created_at.replace(year=2020)
            db.session.commit()

        resp = client.get("/api/tasks")
        data = resp.get_json()
        assert data[-1]["title"] == "Old Task"

    def test_create_task_success(self, client):
        resp = client.post(
            "/api/tasks",
            data=json.dumps({"title": "New Task", "description": "New desc"}),
            content_type="application/json",
        )
        assert resp.status_code == 201
        data = resp.get_json()
        assert data["title"] == "New Task"
        assert data["description"] == "New desc"
        assert data["completed"] is False
        assert "id" in data

    def test_create_task_title_only(self, client):
        resp = client.post(
            "/api/tasks",
            data=json.dumps({"title": "Title Only"}),
            content_type="application/json",
        )
        assert resp.status_code == 201
        data = resp.get_json()
        assert data["title"] == "Title Only"
        assert data["description"] is None

    def test_create_task_missing_title(self, client):
        resp = client.post(
            "/api/tasks",
            data=json.dumps({}),
            content_type="application/json",
        )
        assert resp.status_code == 400
        assert resp.get_json()["error"] == "Title is required"

    def test_create_task_empty_title(self, client):
        resp = client.post(
            "/api/tasks",
            data=json.dumps({"title": "   "}),
            content_type="application/json",
        )
        assert resp.status_code == 400
        assert resp.get_json()["error"] == "Title is required"

    def test_update_task_full(self, client, sample_task):
        resp = client.put(
            f"/api/tasks/{sample_task}",
            data=json.dumps({
                "title": "Updated",
                "description": "Updated desc",
                "completed": True,
            }),
            content_type="application/json",
        )
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["title"] == "Updated"
        assert data["description"] == "Updated desc"
        assert data["completed"] is True

    def test_update_task_partial(self, client, sample_task):
        resp = client.put(
            f"/api/tasks/{sample_task}",
            data=json.dumps({"completed": True}),
            content_type="application/json",
        )
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["completed"] is True

    def test_update_task_empty_title(self, client, sample_task):
        resp = client.put(
            f"/api/tasks/{sample_task}",
            data=json.dumps({"title": "   "}),
            content_type="application/json",
        )
        assert resp.status_code == 400

    def test_update_task_not_found(self, client):
        resp = client.put(
            "/api/tasks/99999",
            data=json.dumps({"title": "Nope"}),
            content_type="application/json",
        )
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "Task not found"

    def test_delete_task_success(self, client, sample_task):
        resp = client.delete(f"/api/tasks/{sample_task}")
        assert resp.status_code == 204

    def test_delete_task_not_found(self, client):
        resp = client.delete("/api/tasks/99999")
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "Task not found"
