from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.handbook import Category
from src.domain.value_objects import CategoryId


class CategoryRepositoryInterface(ABC):
    """Category Repository Interface"""

    @abstractmethod
    def get_all(self) -> List[Category]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, pk: CategoryId) -> Category:
        raise NotImplementedError

    @abstractmethod
    def create(self, category: Category) -> Category:
        raise NotImplementedError

    @abstractmethod
    def update(self, category: Category) -> Category:
        raise NotImplementedError

    @abstractmethod
    def delete(self, pk: CategoryId) -> None:
        raise NotImplementedError
