from django.db import models

# Create your models here.

class Dictionary(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.word} - {self.translation}"


class Registration(models.Model):
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password_conf = models.CharField(max_length=50)
  

    def __str__(self):
        return f"{self.email} {self.first_name} {self.last_name} {self.password} {self.password_conf}"