from django.db import models
from posts.models import Post
from posts.base_models import BaseModels


class Catalog(BaseModels):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Default description")

    def __str__(self):
        return f"{self.name}{self.description}"
