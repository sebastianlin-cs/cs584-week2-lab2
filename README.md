# CS584 Week 2 Lab - Basic Health Tracking Dashboard

## What This Does
An interactive Flask web app that:
- Shows current time and days until weekend
- Collects health data via form (sleep hours, water intake)
- Provides personalized feedback based on input
- Demonstrates GET vs POST requests in Flask

## How to Run Locally

### Step 0. Make sure to create and activate your virtual environment...

```bash
python -m venv venv
source venv/bin/activate
```

### 1. Install Flask
```bash
pip install flask
```

### 2. Run the app
```bash
flask run
```
(or)
```bash
python app.py
```

### 3. Open in browser
Navigate to: `http://localhost:5000`

## Key Concepts We're Exploring

### HTML Forms
- `<form>` with POST method
- Input types: text, number
- Form validation with `required` attribute

### Flask Routes
- **GET route** (`/`): Displays the page
- **POST route** (`/submit`): Handles form submission
- **PRG Pattern**: Post-Redirect-Get (PRG) to prevent duplicate submissions

### Jinja2 Templates
- Conditional rendering: `{% if %}...{% endif %}`
- Variable display: `{{ variable }}`
- Form value persistence: `value="{{ user_data.name or '' }}"`

### In-Memory Data Storage
- Uses Python dictionary to store user data
- **Note**: Data resets when app restarts (not persistent)
- In real apps, you'd use a database (covered later!)

## File Structure
```
cs584-week2-lab-extended/
├── app.py                 # Flask application with routes
├── templates/
│   └── index.html        # HTML template with form
├── static/
│   └── style.css         # Styling
└── README.md             # This file
```

## What You'll Practice Here
- **Collecting user input** (we'll need this for case study)
- **Processing form data** (foundation for common user interfaces)
- **Providing dynamic feedback**
- **GET vs POST** (essential for all web apps)


## Next Steps
In the assignment assigned next, you will be asked to:
- Use feature branches for each added feature
- Create pull requests for each feature
- Track work on a GitHub Project board
- Write better documentation
