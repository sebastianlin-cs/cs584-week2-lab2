"""
Health Dashboard - Flask Application Starter
Your task: Follow LAB_GUIDE.md to add form handling!
"""

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# In-memory storage for user data (we'll add to this during the lab!)
user_data = {}


@app.route('/')
def index():
    """Home page with time/weekend counter"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day_num = datetime.now().weekday()  # Monday=0, Sunday=6
    days_to_weekend = 5 - day_num if day_num < 5 else 0
    
    return render_template('index.html', 
                         time=current_time, 
                         days_to_weekend=days_to_weekend,
                         user_data=user_data)


# TODO: Add /submit route here (see LAB_GUIDE.md Part 3)


if __name__ == '__main__':
    app.run(debug=True)