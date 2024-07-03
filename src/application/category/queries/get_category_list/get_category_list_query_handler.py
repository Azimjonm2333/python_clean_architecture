from typing import List

from automapper import Mapper
from mediatr import Mediator

from src.application.category.queries.get_category_list.get_category_list_query import (
    GetCategoryListQuery,
)
from src.application.category.responses.category_vm import CategoryVm
from src.application.common.contracts.repositories.category_repository_interface import (
    CategoryRepositoryInterface,
)


@Mediator.handler
class GetCategoryListQueryHandler:
    def __init__(self, mapper: Mapper, repository: CategoryRepositoryInterface):
        self.__repository = repository
        self.__mapper = mapper

    def handle(self, request: GetCategoryListQuery) -> List[CategoryVm]:
        db_response = self.__repository.get_all(limit=request.limit)
        return self.__mapper.to(List[CategoryVm]).map(db_response)
