from flask import Flask, jsonify

app = Flask(__name__)

# Simple in-memory task list for assignment
task_list = [
    {"id": 1, "title": "Landing Page Design", "available_slots": 2},
    {"id": 2, "title": "API Testing", "available_slots": 1}
]

@app.route("/")
def home():
    return jsonify({"status": "API running"})


@app.route("/tasks/<int:task_id>/accept", methods=["POST"])
def accept_task(task_id):
    task = next((t for t in task_list if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    if task["available_slots"] == 0:
        return jsonify({"error": "No slots left"}), 400

    task["available_slots"] -= 1

    return jsonify({
        "message": "Task accepted",
        "remaining_slots": task["available_slots"]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
