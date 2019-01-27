

# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, check_log_in, add_job, add_workplace, get_all_students, get_jobs

# Starting the flask app
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('home.html')

# App routing code here
@app.route('/jobspage')
def jobspage():
    if session.get("loggedin") == True:
        return render_template('logged_in.html', jobs=get_jobs())
    else:
        return redirect(url_for("login"))

@app.route('/addpost', methods=['GET','POST'])
def add_job_route():
    if request.method == 'GET':
        return render_template('register_job.html')
    else:
        job_name = request.form["name"]
        job_desc=request.form["desc"]
        job_salary=request.form["salary"]
        job_location=request.form["location"]
        job_min_age=request.form["min_age"]
        job_password=request.form["pwd"] 
        job_email = request.form["Email"]
        job_check_password = request.form["check_pwd"]
        add_job(job_name,job_desc,job_location,job_min_age,job_salary,job_email)
        return redirect(url_for("postspage"))

@app.route('/profile')
def profile():
    return render_template('profile.html', students_profile= get_all_students()) 
    
# Running the Flask app

if __name__ == "__main__":
    app.run(debug=True)



