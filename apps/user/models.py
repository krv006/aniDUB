from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass



# class User(AbstractUser):
#     class Type(TextChoices):
#         OPERATOR = 'operator', 'Operator'
#         ADMIN = 'admin_side', 'Admin_side'
#         USER = 'user', 'User'
#
#     username = None
#     first_name = None
#     last_name = None
#     email = EmailField(unique=True)
#     name = CharField(max_length=255)
#     is_active = BooleanField(default=False)
#     type = CharField(max_length=25, choices=Type.choices, default=Type.USER, verbose_name="user type")
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()