from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = 'postlarst'
        verbose_name_plural = 'postlar'
    nomi = models.CharField(max_length=50)
    daromadi = models.IntegerField()
    def __str__(self):
        return self.nomi ,self.daromadi