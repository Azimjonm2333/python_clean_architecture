from src.domain.value_objects import CategoryId


class CategoryVm:
    def __init__(self, pk: CategoryId, name: str):
        self.pk = pk
        self.name = name
