from django.db.models import Model, CharField


class Film(Model):
    name = CharField(max_length=100)
