from flask import Flask, render_template, request, redirect, url_for, session
import requests
from bs4 import BeautifulSoup

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "secret_key"  # Set a secret key for session management

# Dummy user database (for authentication)
users = {"admin": "password123"}

# Function to get match schedule and results
def get_match_schedule():
    url = "https://www.google.com/search?q=premier+league+schedule"
    headers = {"User -Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Retrieve upcoming matches and results
    upcoming_matches = []
    past_results = []

    # Example selector for upcoming matches (this may need adjustment based on the Google structure)
    for match in soup.select(".BNeawe.iBp4i.AP7Wnd"):
        upcoming_matches.append(match.text)
    
    # Example to capture past results (this may need adjustment based on the Google structure)
    for result in soup.select(".BNeawe.s3v9rd.AP7Wnd"):
        past_results.append(result.text)
    
    return upcoming_matches[:5], past_results[:5]  # Return top 5 upcoming matches and past results

# Route for login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to authenticate user
@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error="Invalid username or password!")

# Route for home page
@app.route('/home')
def home():
    if 'username' in session:
        upcoming_matches, past_results = get_match_schedule()
        return render_template('home.html', username=session['username'], upcoming_matches=upcoming_matches, past_results=past_results)
    return redirect(url_for('login'))

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)