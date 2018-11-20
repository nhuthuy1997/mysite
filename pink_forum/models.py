import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

class Category(models.Model):
  title = models.CharField(max_length=250)
  def __str__(self):
    return self.title

class Moderator(User):
  categories = models.ManyToManyField(Category)

class NormalUser(User):
  banning_categories = models.ManyToManyField(Category)

class Topic(models.Model):
  title = models.CharField(max_length=250)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  status = models.BooleanField(default=0)
  def __str__(self):
    return self.title

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length = 250)
  content = models.TextField(default='')
  status = models.SmallIntegerField(default=0)
  topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
  def __str__(self):
    return self.title

class Vote(PolymorphicModel):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  point = models.SmallIntegerField(default=0)

class VoteTopic(Vote):
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class VotePost(Vote):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
