from django.db import models

# Create your models here.

class Upload(models.Model):
    #image = models.ImageField(upload_to='images')
    image = models.FileField(upload_to='files')

    def __str__(self):
        return str(self.pk)
