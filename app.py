from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Hardcoded secret key (vulnerability)
# Security Fix: Replaced hardcoded secret with environment variable

SECRET_KEY = os.environ.get("SECRET_KEY")


# Mock database
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

import html

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    if task_content:
        # Security Fix: Escaped user input to prevent XSS or HTML injection

        safe_content = html.escape(task_content)
        tasks.append(safe_content)
        return jsonify({"message": "Task added successfully!"}), 200
    return jsonify({"error": "Content cannot be empty!"}), 400

@app.route('/delete', methods=['POST'])
def delete_task():
    index_input = request.form.get('index')

    # Security Fix: Validate input is a digit before converting to integer
    if index_input and index_input.isdigit():
        task_index = int(index_input)
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            return jsonify({"message": "Task deleted successfully!"}), 200
    return jsonify({"error": "Invalid task index!"}), 400

    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        return jsonify({"message": "Task deleted successfully!"}), 200
    return jsonify({"error": "Invalid task index!"}), 400

if __name__ == '__main__':
         # Bandit Fix: Disabled debug mode and allowed external container access
         import os

debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
app.run(debug=debug_mode, host="0.0.0.0", port=5000)



