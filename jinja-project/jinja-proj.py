#!/usr/bin/env python3
from flask import render_template
from flask import request
from flask import Flask
from flask import url_for
from flask import redirect

app = Flask(__name__)

#variables
#blog_id = 0
blog_list=[{
      "title": "Opening Party!",
      "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "author": "yoshi",
      "id": 2
    },
    {
      "title": "title",
      "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "author": "mario",
      "id": 3
    },
    {
      "title": "fsf",
      "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "author": "mario",
      "id": 4
    },
    {
      "title": "this is a blog",
      "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      "author": "yoshi",
      "id": 5
    }]

blog_id = len(blog_list) + 1

#Page types
#Homepage - displays blogs
@app.route("/", methods = ["GET", "DELETE"])
def homepage():
    if request.method == "GET":
        return render_template("index.html", blog_list = blog_list)
    elif request.method == "DELETE":
        del_id = request.get()
        blog_list.remove(del_id)
        return "DELETE BLOG"
#Create - create blogs, POSTs blog objects to blog_ array to be displayed on the homepage
@app.route("/create", methods = ["POST","GET"])
def create_blog():
    if request.method == "POST":
        blog = {}
        blog["title"] = request.form.get("blog_title")
        blog["body"] = request.form.get("blog_body")
        blog["author"] = request.form.get("blog_author")
        #blog["id"] = blog_id
        blog_list.append(blog)
        #blog_id+= 1
        return redirect(url_for('homepage', blog_list = blog_list))
    elif request.method == "GET":
        return render_template("create.html")

#Displays blogs on homepage via blog_array data
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=2224, debug=True)
