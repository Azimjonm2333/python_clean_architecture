from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.handbook import Category
from src.domain.value_objects import CategoryId


class CategoryRepositoryInterface(ABC):
    """Category Repository Interface"""

    @abstractmethod
    def get_all(self, limit: int = 100) -> List[Category]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, pk: CategoryId) -> Category:
        raise NotImplementedError

    @abstractmethod
    def create(self, name: str) -> Category:
        raise NotImplementedError

    @abstractmethod
    def update(self, pk: CategoryId, name: Optional[str]) -> Category:
        raise NotImplementedError

    @abstractmethod
    def delete(self, pk: CategoryId) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, **kwargs) -> bool:
        raise NotImplementedError
