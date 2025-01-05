from django.core.exceptions import ValidationError
import os


def validate_video_format(value):
    valid_extensions = ['.webm', '.mp4', '.avi', '.mkv']
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f"Faqat quyidagi formatlardagi fayllar ruxsat etiladi: {', '.join(valid_extensions)}")
