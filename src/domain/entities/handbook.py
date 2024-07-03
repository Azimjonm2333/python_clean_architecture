from dataclasses import asdict, dataclass

from ..value_objects import CategoryId


@dataclass
class Category:
    category_id: CategoryId
    name: str

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return asdict(self)
