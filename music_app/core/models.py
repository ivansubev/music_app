from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.


def validate_chars_nums_underscore(value):
    INVALID_CHARS_EXCEPTION_MESSAGE = "Ensure this value contains only letters, numbers, and underscore."
    for char in value:
        if isinstance(value, str):
            continue
        elif isinstance(value, int):
            continue
        elif char == "_":
            continue
        else:
            raise ValidationError(INVALID_CHARS_EXCEPTION_MESSAGE)


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_chars_nums_underscore

        )
    )
    email = models.EmailField()
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            MinValueValidator(0),
        )
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30

    ARTIST_NAME_MAX_LEN = 30

    GENRE_MAX_LEN = 30
    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
    )
    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LEN,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=(
            ("pop", "Pop Music"),
            ('jazz', 'Jazz Music'),
            ('r&b', 'R&B Music'),
            ('rock', 'Rock Music'),
            ('country', 'Country Music'),
            ('dance', 'Dance Music'),
            ('hiphop', 'Hip Hop Music'),
            ('other', 'Other')
        )
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )
