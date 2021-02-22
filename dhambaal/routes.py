from flask import render_template, request,redirect 
from dhambaal import app
from dhambaal.models.Post import Post
from dhambaal.models.categories import Category


@app.route("/",methods=['GET','POST'])
def index():
    posts=Post.query.all()
    return render_template("index.html",posts = posts)


@app.route("/comments")

def comments():
    return render_template("comments.html", coments=coments)

@app.route("/admin",methods=['GET','POST'])
def creat_post():
    if request.method == "POST":
        title=request.form.get('title')
        description=request.form.get('description')
        source=request.form.get('source')
        #inserting value to the database
        post1=Post(title=title,description=description,source=source)
        post1.save_to_db()
        return redirect("/")

    return render_template("post_form.html")

@app.route("/category",methods=['GET','POST'])
def creat_cat():
    if request.method == "POST":
        name=request.form.get('name')
        description=request.form.get('description')
        #inserting value to the database
        category=Category(name=name,description=description)
        category.save_to_db()
        
        return redirect("/")

    return render_template("category_form.html")



# def about():
    return render_template("about.html")
