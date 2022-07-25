# Blog Capstone Project Part 3
# Use https://sqliteonline.com/ to see .db files online
import datetime as dt
import os
import smtplib

from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

# notification settings, unchanged from Day 60
SUBJECT_TEXT = "A Message from the Blog Capstone Project"
RECEIVER_NAME = "Niharika Gadde"
OWN_EMAIL = os.environ["My_EMAIL"]
OWN_PASSWORD = os.environ["My_SecretKey"]

app = Flask(__name__)
app.secret_key = "ThisIsASecretKey"
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # this is a CKEditorField
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


def get_current_year():
    """Returns the current year as INT."""
    return dt.datetime.now().year


def get_current_date():
    """Returns the current date as a STR."""
    return dt.datetime.now().strftime("%B %d, %Y")


def send_email(message):
    """Takes a DICT with the details and sends an email to the defined address."""
    # format the email
    sender = f"{message['name']} <{message['email']}>"
    receiver = f"{RECEIVER_NAME} <{OWN_EMAIL}>"
    body = f"Subject: {SUBJECT_TEXT}\nTo: {receiver}\nFrom: {sender}\n\n" \
           f"{message['message']}\n\n" \
           f"From:\nName: {message['name']}\nEmail: {message['email']}\nPhone: {message['phone']}"
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(sender, receiver, body)
    except smtplib.SMTPServerDisconnected as ex:
        print(ex)
        print("Make sure the SMTP_LOGIN and SMTP_PASS credentials have been set correctly in config.py.")
        return False
    else:
        # just to have some feedback
        print(f"A message was sent to {OWN_EMAIL}.")
        return True


@app.route("/")
def home():
    all_posts = BlogPost.query.all()
    return render_template("index.html", posts=all_posts, year=get_current_year())


@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    blog_post = BlogPost.query.get(blog_id)
    if blog_post:
        return render_template("post.html", post=blog_post, year=get_current_year())
    else:
        return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html", year=get_current_year())


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    # display a different page after a message was submitted
    if request.method == "POST":
        message = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "message": request.form["message"]
        }
        # try to send the message
        if send_email(message):
            status = "Success!"
            text = "Your message has been sent."
        else:
            status = "Something went wrong."
            text = "The message could not be sent."
        # display the status page
        return render_template("message.html", status=status, text=text)
    # display the regular contact page
    else:
        return render_template("contact.html", year=get_current_year())


@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=get_current_date(),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    return render_template("make-post.html", heading="New Post", form=form, year=get_current_year())


@app.route("/edit/<int:blog_id>", methods=["GET", "POST"])
def edit_post(blog_id):
    # find the blog in the DB
    post = BlogPost.query.get(blog_id)
    # if the post exists, fill in the fields in the form
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    # update the DB
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        # redirect to the post page
        return redirect(f"/post/{post.id}")
    return render_template("make-post.html", heading="Edit Post", form=edit_form, year=get_current_year())


@app.route("/delete/<int:blog_id>", methods=["GET", "POST"])
def delete_post(blog_id):
    post = BlogPost.query.get(blog_id)
    # if such posts exists, delete it
    if post:
        db.session.delete(post)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    # redirect to the main page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
