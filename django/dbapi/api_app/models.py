from django.db import models

# Create your models here.

class Article(models.Model):
  # translations for all languages are tied together with md5 of english
  md5hash = models.CharField(max_length=32)

  # language code
  langCode = models.CharField(max_length=4)

  # actual sentence in the given language
  article = models.CharField(max_length=2000)

  constraints = [
    models.UniqueConstraint(fields=['md5hash', 'langCode'], name='unique translation for language')
  ]
# end class