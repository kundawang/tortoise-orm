"""
This is the testing Models — on_delete=NO_ACTION relations
"""

from tortoise import fields
from tortoise.models import Model


class Author(Model):
    name = fields.CharField(max_length=50)


class Book(Model):
    author: fields.ForeignKeyRelation[Author] = fields.ForeignKeyField(
        "models.Author", related_name="books", on_delete=fields.NO_ACTION
    )


class Profile(Model):
    author: fields.OneToOneRelation[Author] = fields.OneToOneField(
        "models.Author", related_name="profile", on_delete=fields.OnDelete.NO_ACTION
    )


class Tag(Model):
    name = fields.CharField(max_length=50)


class Article(Model):
    tags: fields.ManyToManyRelation[Tag] = fields.ManyToManyField(
        "models.Tag", related_name="articles", on_delete=fields.NO_ACTION
    )
