from django.db import models

class Categorie(models.Model):
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    pub_date = models.DateField('date published')
    category = models.ForeignKey(Categorie)
    def __str__(self):              # __unicode__ on Python 2
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    body = models.TextField()
    def __str__(self):              # __unicode__ on Python 2
        return self.title