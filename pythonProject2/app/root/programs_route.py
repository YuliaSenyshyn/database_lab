from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import programs_controller
from ..domain.programs import Program
from app.domain.program_days import ProgramDay

program_bp = Blueprint('program', __name__, url_prefix='/program')

@program_bp.route('', methods=['GET'])
def get_all_programs():
    return make_response(jsonify(programs_controller.find_all()), HTTPStatus.OK)

@program_bp.route('', methods=['POST'])
def create_program() -> Response:
    content = request.get_json()
    program = Program.create_from_dto(content)
    programs_controller.create(program)
    return make_response(jsonify(program.put_into_dto()), HTTPStatus.CREATED)

@program_bp.route('/<int:program_id>', methods=['GET'])
def get_program(program_id: int) -> Response:
    program = programs_controller.find_by_id(program_id)
    if program is None:
        return make_response({"message": "Program not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(program), HTTPStatus.OK)

@program_bp.route('/<int:program_id>', methods=['PUT'])
def update_program(program_id: int) -> Response:
    content = request.get_json()
    program = Program.create_from_dto(content)
    programs_controller.update(program_id, program)
    return make_response("Program updated", HTTPStatus.OK)

@program_bp.route('/<int:program_id>', methods=['PATCH'])
def patch_program(program_id: int) -> Response:
    content = request.get_json()
    programs_controller.patch(program_id, content)
    return make_response("Program updated", HTTPStatus.OK)

@program_bp.route('/<int:program_id>', methods=['DELETE'])
def delete_program(program_id: int) -> Response:
    programs_controller.delete(program_id)
    return make_response("Program deleted", HTTPStatus.OK)


