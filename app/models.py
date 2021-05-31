from app.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    letters = db.relationship("Letter", secondary="users_letters")

    def __str__(self):
        return self.email


class Letter(db.Model):
    __tablename__ = "letters"

    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship("User", secondary="users_letters")
    name = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(84), nullable=False, index=True)
    send_email = db.Column(db.String(84), nullable=False, index=True)
    reference_id = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"reference: {self.reference_id}"


class UserLetter(db.Model):
    __tablename__ = "users_letters"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    letter_id = db.Column(db.Integer, db.ForeignKey("letters.id"), nullable=False)
    user = db.relationship(User, backref="users_letters")
    letter = db.relationship(Letter, backref="users_letters")
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"users_letters: {self.id}"
