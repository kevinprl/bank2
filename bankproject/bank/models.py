from django.db import models

# Create your models here.
class team(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

#dependent dropdown


class Branch(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class City(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name