from django import forms
from photos.models import Photo
from photos.settings import BADWORDS
from django.core.validators import ValidationError

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ("owner",)

    def clean(self):
        cleaned_data = super(PhotoForm, self).clean()

        description = cleaned_data.get("description", "")

        for badword in BADWORDS:
            if badword in description:
                raise ValidationError("Palabra no permitida")

        return cleaned_data