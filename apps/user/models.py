from django.db import models
# import mongoengine
# Create your models here.


class CorpusManager(models.Model):
    login_name = models.CharField(max_length=24)
    password = models.CharField(max_length=24)
    user_name = models.CharField(max_length=24)
    authority = models.CharField(default=0, max_length=24)



