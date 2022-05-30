from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Create your models here.

def validate_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))
    
class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)


class Picturesque(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    genre = models.ForeignKey(Genre, null=True, on_delete = models.SET_NULL)
    date = models.DateTimeField()