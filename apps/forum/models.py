from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Topics
class Category(models.Model):
    text = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.text

#Subtopics
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Category, on_delete=True,blank = True,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

#Posts
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."

class Comments(models.Model):
    text = models.TextField()
    title = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    def __str__(self):
        return self.text