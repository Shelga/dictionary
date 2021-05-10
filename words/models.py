from django.db import models

# Create your models here.

class New_user(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password_conf = models.CharField(max_length=50)
    bearer_token = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.password} {self.password_conf}"

class DictionaryLine(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    # user = models.ForeignKey(New_user, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.word} - {self.translation}"


