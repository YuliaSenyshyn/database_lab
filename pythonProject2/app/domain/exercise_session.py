from __future__ import annotations
from app import db


class ExerciseSession(db.Model):
    __tablename__ = 'exercise_session'

    id = db.Column('session_id', db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('program_assignment.assignment_id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'))
    session_date = db.Column(db.Date, nullable=False)

    assignment = db.relationship('ProgramAssignment')
    exercise = db.relationship('Exercise', back_populates='exercise_sessions')

    @staticmethod
    def create_from_dto(dto):
        return ExerciseSession(
            assignment_id=dto['assignment_id'],
            exercise_id=dto['exercise_id'],
            session_date=dto['session_date']
        )

    def put_into_dto(self):
        return {
            'session_id': self.id,
            'assignment_id': self.assignment_id,
            'exercise_id': self.exercise_id,
            'session_date': self.session_date.isoformat()
        }