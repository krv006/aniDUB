from django.contrib import admin

from film.models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass