from datetime import datetime
from dhambaal import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    source = db.Column(db.String(120), nullable=False)
    #category = db.Column(db.String(120), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'Post ({self.title}, {self.description})'
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# CREATE TABLE 'posts' (id int primarykey, title varchar(120), description text   )


