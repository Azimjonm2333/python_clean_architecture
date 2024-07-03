from django.db import models


class Category(models.Model):
    name: str = models.CharField(verbose_name="Название", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
