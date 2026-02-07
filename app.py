from flask import Flask, jsonify

app = Flask(__name__)

# -------------------------
# In-memory task storage
# -------------------------
tasks = [
    {"id": 1, "title": "Design Landing Page", "slots": 2},
    {"id": 2, "title": "API Testing", "slots": 1}
]

# -------------------------
# Home route (test)
# -------------------------
@app.route("/")
def home():
    return jsonify({"message": "Task 8 API is running"})

# -------------------------
# Task Acceptance API
# -------------------------
@app.route("/tasks/<int:task_id>/accept", methods=["POST"])
def accept_task(task_id):

    # 1️⃣ Find task
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    # 2️⃣ Check slot availability
    if task["slots"] <= 0:
        return jsonify({"error": "No slots available"}), 400

    # 3️⃣ Accept task → reduce slot
    task["slots"] -= 1

    return jsonify({
        "message": "Task accepted successfully",
        "remaining_slots": task["slots"]
    }), 200


# -------------------------
# Run server
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
