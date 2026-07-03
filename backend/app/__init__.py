from flask import Flask, jsonify
from flask_cors import CORS
from app.config import config_map
from app.models import db


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config_map.get(config_name, config_map["default"]))
    CORS(app)
    db.init_app(app)

    @app.route("/")
    def index():
        return jsonify({
            "app": "Task Manager API",
            "version": "1.0.0",
            "endpoints": {
                "GET /api/tasks": "List all tasks",
                "POST /api/tasks": "Create a task",
                "PUT /api/tasks/<id>": "Update a task",
                "DELETE /api/tasks/<id>": "Delete a task",
            },
        })

    with app.app_context():
        from app.routes import tasks
        app.register_blueprint(tasks.bp)

        from app.error_handlers import register_error_handlers
        register_error_handlers(app)

        db.create_all()

    return app
