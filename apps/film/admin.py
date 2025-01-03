from django.contrib import admin

from film.models import Episode, Anime, Frame


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    inlines = EpisodeInline,


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    pass
