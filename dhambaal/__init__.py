from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dhambaal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

# posts = [
#     {"title":"What is Lorem Ipsum?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"},
#     {"title":"Where does it come from?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"},
#     {"title":"Why do we use it?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"},
#     {"title":"Where can I get some?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"}     
# ]

# coments = [
#     {"author":"Ahmed","message":"Contrary to popular belief, Lorem Ipsum is not simply random text. "},
#     {"author":"Faatima","message":"Contrary to popular belief, Lorem Ipsum is not simply random text. "},
#     {"author":"Aisha","message":"Contrary to popular belief, Lorem Ipsum is not simply random text. "},
#     {"author":"Farah","message":"Contrary to popular belief, Lorem Ipsum is not simply random text. "},
#     {"author":"Abdi","message":"Contrary to popular belief, Lorem Ipsum is not simply random text. "}
# ]
# 
# @app.route("/")
# def index():
#     return {"Message":"Success","content":"Hello Flask"}

from dhambaal import routes