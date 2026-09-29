from django.db import models

# # Create your models here.

# class PublishedModel(models.Model):
#     is_published = models.BooleanField(default=True)
#     title = models.CharField(max_length=256)
#     slug = models.SlugField(max_length=64, unique=True)

#     class Meta:
#         abstract = True


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True
