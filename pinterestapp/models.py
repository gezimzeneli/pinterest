from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    firstname = models.CharField(max_length=255, default='')
    familyname = models.CharField(max_length=255, default='')
    image_url = models.CharField(max_length=2083, default='')


class ImageBoard(models.Model):
    userID = models.IntegerField()
    title = models.CharField(max_length=255, default='')


class Image(models.Model):
    image_url = models.CharField(max_length=2083, default='')
    title = models.CharField(max_length=255, default='')
    origin_url = models.CharField(max_length=2083, default='')


class Followers(models.Model):
    user_who_followes = models.IntegerField()
    user_who_gets_followed = models.IntegerField()


class Likes(models.Model):
    imageID = models.IntegerField()
    userID = models.IntegerField()


class Comment(models.Model):
    text = models.TextField()
    imageID = models.IntegerField()
    userID = models.IntegerField()


class AssignedImagesToBoard(models.Model):
    imageID = models.IntegerField()
    boardID = models.IntegerField()