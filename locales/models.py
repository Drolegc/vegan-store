from django.db import models

# Create your models here.

class Local(models.Model):

    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    image = models.ImageField(upload_to="locales",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name
    