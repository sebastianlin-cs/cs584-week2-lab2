"""
Health Dashboard - Flask Application Starter
Your task: Follow LAB_GUIDE.md to add form handling!
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for user data (we'll add to this during the lab!)
user_data = {
    "name": "",
    "sleep_hours": "",
    "water_glasses": "",
    "exercise_minutes": ""
}


@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day_num = datetime.now().weekday()
    days_to_weekend = 5 - day_num if day_num < 5 else 0
    
    return render_template('index.html', 
                         time=current_time, 
                         days_to_weekend=days_to_weekend,
                         user_data=user_data)  # <- NEW!


# TODO: Add /submit route here (see LAB_GUIDE.md Part 3)
@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission"""
    # Get form data
    name = request.form.get('name', '')
    sleep_hours = request.form.get('sleep_hours', '')
    water_glasses = request.form.get('water_glasses', '')
    exercise_minutes = request.form.get('exercise_minutes', '')

    
    # Store it
    user_data['name'] = name
    user_data['sleep_hours'] = sleep_hours
    user_data['water_glasses'] = water_glasses
    user_data['exercise_minutes'] = exercise_minutes

    
    # Generate feedback
    try:
        hours = float(sleep_hours)
        if hours < 7:
            user_data['feedback_sleep_hours'] = "⚠️ Try to get more sleep!"
        else:
            user_data['feedback_sleep_hours'] = "✅ Great sleep!"
    except ValueError:
        user_data['feedback_sleep_hours'] = "Please enter valid hours."
    
    try:
        cups = float(water_glasses)
        if cups < 7:
            user_data['feedback_water_glasses'] = "⚠️ Do you feel thirsty?"
        else:
            user_data['feedback_water_glasses'] = "✅ Good job!"
    except ValueError:
        user_data['feedback_water_glasses'] = "Please enter valid glasses."

    try:
        mins = float(exercise_minutes)
        if mins == 0:
            user_data['feedback_exercise_minutes'] = "🧘 Rest day is fine — try a short walk if you can."
        elif mins < 20:
            user_data['feedback_exercise_minutes'] = "👍 Nice start — aim for 20+ minutes."
        elif mins <= 60:
            user_data['feedback_exercise_minutes'] = "✅ Great work — solid activity level!"
        else:
            user_data['feedback_exercise_minutes'] = "🔥 Awesome — remember to hydrate and recover."
    except ValueError:
        user_data['feedback_exercise_minutes'] = "Please enter valid minutes."

    
    print("DEBUG - Data stored:", user_data) # <-- Show your collected variable in terminal.
    # ... it's being stored as an in-memory Python dict... it's not going to an API or database yet! We'll work on that in a future lecture.

    # Redirect back to home
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)