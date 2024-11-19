from __future__ import annotations
from typing import Dict, Any
from app import db


# Клас для таблиці programs
class Program(db.Model):
    __tablename__ = 'programs'
    id = db.Column('program_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(45))
    program_day_id = db.Column(db.Integer, db.ForeignKey('program_days.program_day_id'))

    day = db.relationship(
        'ProgramDay',
        back_populates='program',
        uselist=False
    )

    # Relationship to ProgramsHasExercise
    exercises = db.relationship(
        'ProgramsHasExercise',  # Use string-based reference
        back_populates='program',  # This should match the name in the ProgramsHasExercise class
        lazy='dynamic',
        cascade='all, delete-orphan'
    )

    @staticmethod
    def create_from_dto(dto):
        return Program(
            name=dto['name'],
            description=dto.get('description'),
            program_day_id=dto['program_day_id']
        )

    def put_into_dto(self):
        return {
            'program_id': self.id,
            'name': self.name,
            'description': self.description,
            'program_day_id': self.program_day_id
        }