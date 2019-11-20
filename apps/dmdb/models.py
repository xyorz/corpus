from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    nickName = models.CharField(max_length=64)
    pwd = models.CharField(max_length=64)
    level = models.IntegerField(default=0)
    presets = models.ManyToManyField('AuthorsInfo', through='UserAuthorsInfoPreset')


class AuthorsInfo(models.Model):
    name = models.CharField(max_length=256)
    dynasty = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    color = models.CharField(max_length=64)
    area = models.CharField(max_length=64, default='未知')
    detail = models.CharField(max_length=4096, default='')


class UserAuthorsInfoPreset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    authorInfo = models.ForeignKey(AuthorsInfo, on_delete=models.CASCADE)


class ZhToHant(models.Model):
    zh = models.CharField(max_length=255)
    hant = models.CharField(max_length=256)


class Var(models.Model):
    key = models.CharField(max_length=64, primary_key=True)
    value = models.CharField(max_length=4096)



