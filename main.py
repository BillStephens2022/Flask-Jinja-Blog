from flask import Flask, render_template
import requests
from post import Post
import datetime

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

current_year = datetime.datetime.now().year

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects, current_year=current_year)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
