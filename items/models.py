from django.db import models

from locales.models import Local

# Create your models here.

class Items(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="items",blank=True, null=True)
    local = models.ForeignKey(Local, verbose_name=("Local"), on_delete=models.CASCADE)
    fiabilidad_plus = models.IntegerField(default=0)
    fiabilidad_minus = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name
    