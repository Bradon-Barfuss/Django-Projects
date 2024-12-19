from django.db import models

# Create your models here.
class BookData(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='images', default='images/none/default.jpg')

    def __str__(self):
        return self.name
