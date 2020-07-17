from django.db import models

# Create your models here.
class Temp(models.Model):
    city = models.CharField(max_length=25)
    temp = models.IntegerField(default=0)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return self.city

    def __str__(self):
        return self.temp

    def __str__(self):
        return self.date

    class Meta:
        verbose_name_plural = 'temps'