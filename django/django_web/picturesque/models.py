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
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        ordering = ("name", "genre")
    def __str__(self):
        return self.name + ", " + str(self.genre) + " - " + str(self.date)
    def as_json(self):
        return dict(
            id=self.id, genre=self.genre,
            date=self.date)
    