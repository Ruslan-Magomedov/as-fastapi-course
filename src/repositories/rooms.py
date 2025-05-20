from src.repositories.base import BaseRepositories
from src.models.rooms import RoomsOrm


class RoomsRepositories(BaseRepositories):
    model = RoomsOrm
