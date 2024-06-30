from django.db import models

class Orphan(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    birthdate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='images',null=True, blank=True)
    details = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Guardian(models.Model):
    orphans = models.ForeignKey(Orphan, on_delete=models.SET_NULL, null=True, related_name='guardians')
    name = models.CharField(max_length=50)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name








