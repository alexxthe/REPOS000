#from django.db import models

# Create your models here.

from django.db import models

class SummitTalk(models.Model):
    Summit_Title = models.CharField(max_length=200)
    Summitor_Name = models.CharField(max_length=100)
    Summitor_Bio = models.TextField()
    Summit_Text = models.URLField()
    Summitor_Photo = models.ImageField(upload_to='images/')
    PUB_DATE_TIME = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Summit_Title


class LeaderTalk(models.Model):
    Blog_Title = models.CharField(max_length=200)
    BlogorName = models.CharField(max_length=100)
    Blog_TEXT = models.TextField()
    BlogorPhoto = models.ImageField(upload_to='images/')
    PUB_DATE_TIME = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Blog_Title
