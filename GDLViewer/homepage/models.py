from django.db import models

# Create your models here.
class URL(models.Model):
    url = models.CharField(max_length=2048)
    def __str__(self):
        return self.url
    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        db_table = 'URL'