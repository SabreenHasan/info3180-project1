"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, filefolder
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app.forms import LoginForm
from app.models import UserProfile
from werkzeug.utils import secure_filename
import os
from datetime import datetime


def get_uploaded_images():
    user_images = os.listdir(filefolder)
    image = []
    for y in user_images:
        s, t = y.split(".")
        if t == "jpg" or t == "png":
            image.append(y)
    return image


@app.route('/')
def home():
    """Render the website's home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods = ["GET", "POST"])
def profile():
    """Render the website's add profile page."""
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        now = datetime.datetime.now()
        firstname = form.firstname.data
        lastname = form.lastname.data
        gender = form.gender.data
        location = form.location.data
        email = form.email.data
        biography = form.biography.data
        s = form.upload.data
        filename = secure_filename(s.filename)
        user = UserProfile(firstname = firstname, lastname = lastname, gender = gender, email = email, location = location, biography = biography, image_name=filename, date_created=now)
        db.session.add(user)
        db.session.commit()
        s.save(os.path.join(filefolder, filename))
            
        flash('User Successfully Added!', 'success')
        return redirect(url_for('profiles'))

    return render_template('profile.html', form=form)


@app.route('profiles')
def profiles():
    """Render the website's view all profiles page."""
    user_images = get_uploaded_images()
    users = UserProfile.query.all()
    return render_template('profiles.html', users=users, user_images=user_images)


@app.route('profile/<userID>')
def user_profiles(userID):
    """Render the website's view all profiles page by the user's ID."""
    user = UserProfile.query.filter_by(user_id=userID).first()
    user_images = get_uploaded_images()
    return render_template('user_profile.html', user=user, user_images=user_images)


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    """Login authentication"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = "Invalid username"
        elif request.form['password'] != app.config['PASSWORD']:
            error = "Invalid password"
        else: 
            session['logged_in'] = True
            flash ('You were successfully logged in')
            return redirect(url_for('home'))
  
    return render_template('login.html', error=error)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


def flash_errors(form):
    """Display error message for incorrect field"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'danger')
 
 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")