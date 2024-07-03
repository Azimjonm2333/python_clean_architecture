from typing import List, Optional

from src.application.common.contracts.repositories.category_repository_interface import (
    CategoryRepositoryInterface,
)
from src.domain.entities.handbook import Category
from src.domain.value_objects import CategoryId

from ...application.common.exceptions.entity_exceptions import EntityAlreadyExists
from ..models import Category as CategoryModel
from .utils import repository_setup

repository_setup()


class CategoryRepository(CategoryRepositoryInterface):
    def get_all(self, limit: int = 100) -> List[Category]:
        instance_list = CategoryModel.objects.all()[:limit]
        return [self.__decode_model(instance) for instance in instance_list]

    def create(self, name: str) -> Category:
        if self.exists(name=name):
            raise EntityAlreadyExists("Category already exists")

        instance = CategoryModel(name=name)
        instance.save()
        return self.__decode_model(instance)

    def update(self, pk: CategoryId, name: Optional[str]) -> Category:
        instance = CategoryModel.objects.get(pk=pk)
        if name:
            instance.name = name
        instance.save()
        return self.__decode_model(instance)

    def get_by_id(self, pk: CategoryId) -> Category:
        instance = CategoryModel.objects.get(pk=pk)
        return self.__decode_model(instance)

    def delete(self, pk: CategoryId) -> None:
        instance = CategoryModel.objects.get(pk=pk)
        instance.delete()

    def exists(self, **kwargs) -> bool:
        return CategoryModel.objects.filter(**kwargs).exists()

    @staticmethod
    def __decode_model(instance: CategoryModel) -> Category:
        return Category(
            category_id=instance.pk,
            name=instance.name,
        )
