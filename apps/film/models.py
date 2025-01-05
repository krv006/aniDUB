from django.db.models import Model, CharField, DateTimeField, TextField, ImageField, FileField, ForeignKey, CASCADE, \
    IntegerField

from shared.utils import validate_video_format


class Anime(Model):
    name = CharField(
        max_length=100,
        verbose_name="Anime nomi",
        help_text="Anime nomini kiriting",
    )
    director = CharField(
        max_length=100,
        verbose_name="Rejissyor",
        help_text="Rejissyor nomini kiriting",
    )
    description = TextField(verbose_name="Tavsif", help_text="Anime haqida qisqacha tavsif", )
    anime_image = ImageField(
        upload_to='film/anime_images/',
        verbose_name="Anime rasmi",
        help_text="Anime uchun asosiy rasm yuklang",
    )
    trailer = FileField(
        upload_to='film/anime_video/',
        verbose_name="Treyler",
        help_text="Anime uchun video treyler yuklang",
        validators=[validate_video_format],
        null=True,
        blank=True,
    )
    banner = ImageField(
        upload_to='film/banners/',
        verbose_name="Banner rasmi",
        help_text="Banner rasmi yuklang",
        null=True,
        blank=True,
    )
    created = DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan sana",
    )

    def __str__(self):
        return self.name


class Frame(Model):
    anime = ForeignKey('film.Anime', CASCADE, related_name="frames", verbose_name="Anime")
    image = ImageField(upload_to="frames/", verbose_name="Kadr rasmi")
    uploaded_at = DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqt")

    def __str__(self):
        return f"Kadr - {self.anime.name}"


class Episode(Model):
    anime = ForeignKey(
        'Anime',
        on_delete=CASCADE,
        related_name="episodes",
        verbose_name="Anime",
        help_text="Qaysi animega tegishli ekanligini belgilang",
    )
    episode_number = IntegerField(
        verbose_name="Qism raqami",
        help_text="Qism raqamini kiriting (masalan, 1, 2, 3...)",
    )
    title = CharField(
        max_length=200,
        verbose_name="Qism nomi",
        help_text="Qism nomini kiriting",
    )
    duration = IntegerField(
        verbose_name="Davomiylik (daqiqa)",
        help_text="Qism davomiyligini daqiqalarda kiriting",
    )
    video_file = FileField(
        upload_to="episodes/videos/",
        verbose_name="Qism video fayli",
        help_text="Qism uchun video fayl yuklang",
    )

    def __str__(self):
        return f"{self.anime.name} - Qism {self.episode_number}: {self.title}"