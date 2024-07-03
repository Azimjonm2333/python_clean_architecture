from dataclasses import asdict, dataclass
from typing import Optional

from ..value_objects import CategoryId, ProductId


@dataclass
class Category:
    category_id: CategoryId
    name: str
    description: str

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return asdict(self)


@dataclass
class Product:
    product_id: ProductId
    name: str
    description: Optional[str]
    price: float
    category: Category

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return asdict(self)
