from flask import Blueprint, request, jsonify
from models.db import conn, cursor

tasks_bp = Blueprint("tasks", __name__)

# GET /tasks
@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    cursor.execute("SELECT id, title FROM tasks")
    rows = cursor.fetchall()
    tasks = [{"id": row[0], "title": row[1]} for row in rows]
    return jsonify(tasks)

# POST /tasks
@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")

    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()

    task_id = cursor.lastrowid
    return jsonify({"id": task_id, "title": title}), 201

# PUT /tasks/<id>
@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    title = data.get("title")

    cursor.execute("UPDATE tasks SET title=? WHERE id=?", (title, task_id))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"id": task_id, "title": title})

# DELETE /tasks/<id>
@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted"})
