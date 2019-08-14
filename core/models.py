from django.db.models import Model, CharField, DateField, TextField, OneToOneField, IntegerField, CASCADE, \
                             DateTimeField
from django.contrib.postgres.fields import JSONField


class Category(Model):
    """
    Category of the Favorite things selectable by the AppUser
    """

    title = CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.title


class FavoriteThing(Model):
    """
    Model to store favorite things of the AppUser
    """

    title = CharField(max_length=255, unique=True, null=False)
    description = TextField()
    rank = IntegerField(null=False)
    metadata = JSONField(null=True)
    category = OneToOneField(Category, primary_key=True, on_delete=CASCADE)
    created_date = DateField(auto_now=True)
    modified_date = DateField(auto_now=False, null=True)

    def __str__(self):
        return self.title


class AuditLog(Model):
    """
    Model to store changes on data
    """

    description = TextField(null=False)
    created_time = DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[:42]
