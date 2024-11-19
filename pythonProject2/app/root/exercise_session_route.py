from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import exercise_session_controller
from ..domain.exercise_session import ExerciseSession

exersice_session_bp = Blueprint('exercise-session', __name__, url_prefix='/exercise-session')

@exersice_session_bp.route('', methods=['GET'])
def get_all_exercise_sessions():
    return make_response(jsonify(exercise_session_controller.find_all()), HTTPStatus.OK)

@exersice_session_bp.route('', methods=['POST'])
def create_exercise_session() -> Response:
    content = request.get_json()
    exercise_session = ExerciseSession.create_from_dto(content)
    exercise_session_controller.create(exercise_session)
    return make_response(jsonify(exercise_session.put_into_dto()), HTTPStatus.CREATED)

@exersice_session_bp.route('/<int:session_id>', methods=['GET'])
def get_exercise_session(session_id: int) -> Response:
    exercise_session = exercise_session_controller.find_by_id(session_id)
    if exercise_session is None:
        return make_response({"message": "Exercise Session not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(exercise_session), HTTPStatus.OK)

@exersice_session_bp.route('/<int:session_id>', methods=['PUT'])
def update_exercise_session(session_id: int) -> Response:
    content = request.get_json()
    exercise_session = ExerciseSession.create_from_dto(content)
    exercise_session_controller.update(session_id, exercise_session)
    return make_response("Exercise Session updated", HTTPStatus.OK)

@exersice_session_bp.route('/<int:session_id>', methods=['PATCH'])
def patch_exercise_session(session_id: int) -> Response:
    content = request.get_json()
    exercise_session_controller.patch(session_id, content)
    return make_response("Exercise Session updated", HTTPStatus.OK)

@exersice_session_bp.route('/<int:session_id>', methods=['DELETE'])
def delete_exercise_session(session_id: int) -> Response:
    exercise_session_controller.delete(session_id)
    return make_response("Exercise Session deleted", HTTPStatus.OK)
