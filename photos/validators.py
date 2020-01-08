from photos.settings import BADWORDS
from django.core.exceptions import ValidationError


def badwords_detector(value):

    for badword in BADWORDS:
        if badword in value:
            raise ValidationError("Palabra no permitida")

    return True
