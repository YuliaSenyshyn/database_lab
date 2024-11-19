from __future__ import annotations
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('users_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    registration_data = db.Column(db.Date)

    trainers = db.relationship('Trainer', secondary='trainers_has_users', back_populates='users', overlaps='users')



    @staticmethod
    def create_from_dto(dto):
        return User(
            first_name=dto['first_name'],
            last_name=dto['last_name'],
            email=dto['email'],
            registration_data=dto['registration_data']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'registration_data': self.registration_data
        }
