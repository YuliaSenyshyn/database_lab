from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import program_assignment_controller
from ..domain.program_assignment import ProgramAssignment

program_assignment_bp = Blueprint('program_assignment', __name__, url_prefix='/program-assignment')

@program_assignment_bp.route('', methods=['GET'])
def get_all_program_assignments():
    return make_response(jsonify(program_assignment_controller.find_all()), HTTPStatus.OK)

@program_assignment_bp.route('', methods=['POST'])
def create_program_assignment() -> Response:
    content = request.get_json()
    program_assignment = ProgramAssignment.create_from_dto(content)
    program_assignment_controller.create(program_assignment)
    return make_response(jsonify(program_assignment.put_into_dto()), HTTPStatus.CREATED)

@program_assignment_bp.route('/<int:assignment_id>', methods=['GET'])
def get_program_assignment(assignment_id: int) -> Response:
    program_assignment = program_assignment_controller.find_by_id(assignment_id)
    if program_assignment is None:
        return make_response({"message": "Program Assignment not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(program_assignment), HTTPStatus.OK)

@program_assignment_bp.route('/<int:assignment_id>', methods=['PUT'])
def update_program_assignment(assignment_id: int) -> Response:
    content = request.get_json()
    program_assignment = ProgramAssignment.create_from_dto(content)
    program_assignment_controller.update(assignment_id, program_assignment)
    return make_response("Program Assignment updated", HTTPStatus.OK)

@program_assignment_bp.route('/<int:assignment_id>', methods=['PATCH'])
def patch_program_assignment(assignment_id: int) -> Response:
    content = request.get_json()
    program_assignment_controller.patch(assignment_id, content)
    return make_response("Program Assignment updated", HTTPStatus.OK)

@program_assignment_bp.route('/<int:assignment_id>', methods=['DELETE'])
def delete_program_assignment(assignment_id: int) -> Response:
    program_assignment_controller.delete(assignment_id)
    return make_response("Program Assignment deleted", HTTPStatus.OK)
