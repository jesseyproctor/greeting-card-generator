from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint

access_options = (('private','private'),
('public', 'public'),)


class User(AbstractUser):
    name= models.CharField(max_length=255)
    
     

class Card(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="cards" )
    message = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=100,  default="", null =True)
    color = models.CharField(max_length=100,  blank=True, null=True)
    style = models.CharField(max_length=100, default="", null=True)
    font = models.CharField(max_length=100, default="", null=True)
    weight = models.CharField(max_length=100, default="", null=True)
    alignment = models.CharField (max_length=100, default="", null=True)
    textboxalignment = models.CharField(max_length=100, default="", null=True)
    image = models.URLField(blank=True, null=True)
    access = models.CharField(max_length=100, choices=access_options, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    textbackgroundopacity = models.CharField(max_length=255, blank=True, null=True)
    backgroundopacity= models.CharField(max_length=255, blank=True, null=True)
    backgroundcolor = models.CharField(max_length=255, blank=True, null=True)
    textbackgroundcolor =models.CharField(max_length=255, blank=True, null=True)


class UserFollowing(models.Model):
    #fromuser is the logged in user who is following
    touser = models.ForeignKey(User,related_name="followers", on_delete=models.CASCADE)
    fromuser = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fromuser','touser'],  name="unique_followers")
        ]

        ordering = ["-created"]

    



 