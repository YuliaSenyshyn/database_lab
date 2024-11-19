from __future__ import annotations
from app import db

class Trainer(db.Model):
    __tablename__ = 'trainers'

    id = db.Column('trainer_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)

    users = db.relationship('User', secondary='trainers_has_users', back_populates='trainers', overlaps='trainers')


    @staticmethod
    def create_from_dto(dto):
        return Trainer(
            first_name=dto['first_name'],
            last_name=dto['last_name'],
            email=dto['email']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
