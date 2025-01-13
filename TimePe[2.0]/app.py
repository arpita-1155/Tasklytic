from flask import Flask, render_template

app = Flask(__name__)

# Route to display the mobile app UI
@app.route('/')
def home():
    return render_template('index.html')  # This will render your HTML file

# Example route for handling tasks (just an example backend logic)
@app.route('/tasks')
def tasks():
    # In a real app, this would be fetched from a database
    task_list = [
        {"id": 1, "title": "Task 1", "description": "Complete wireframe design."},
        {"id": 2, "title": "Task 2", "description": "Prepare for the presentation."},
        {"id": 3, "title": "Task 3", "description": "Revise project milestones."}
    ]
    return render_template('tasks.html', tasks=task_list)  # Display tasks in another HTML page

if __name__ == '__main__':
    app.run(debug=True)
