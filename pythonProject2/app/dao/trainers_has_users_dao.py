from app.domain import TrainersHasUsers
from app.dao.general_dao import GeneralDAO

class TrainerHasUserDAO(GeneralDAO):
    _domain_type = TrainersHasUsers
