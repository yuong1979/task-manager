from flask import Blueprint, jsonify, request
from app.models import db, Task

bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")


@bp.route("", methods=["GET"])
def list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([t.to_dict() for t in tasks])


@bp.route("", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not data.get("title", "").strip():
        return jsonify({"error": "Title is required"}), 400
    task = Task(
        title=data["title"].strip(),
        description=data.get("description", "").strip() or None,
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 200


@bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    if "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title is required"}), 400
        task.title = data["title"].strip()
    if "description" in data:
        task.description = data["description"].strip() or None
    if "completed" in data:
        task.completed = bool(data["completed"])
    db.session.commit()
    return jsonify(task.to_dict())


@bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return "", 204
