from django.db import models

# Create your models here.
class Disorder(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)

class Story(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    content = models.CharField(max_length=5000, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=25, blank=True, unique=False)
    disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)

class BlogPost(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    content = models.CharField(max_length=5000, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=25, blank=True, unique=False)
    disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.title)

class LocalResource(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    img_url = models.CharField(max_length=500, blank=True, unique=False)
    url = models.CharField(max_length=500, blank=True, unique=False)
    address = models.CharField(max_length=100, blank=True, unique=False)
    phone = models.CharField(max_length=20, blank=True, unique=False)
    description = models.CharField(max_length=1000, blank=True, unique=False)
    disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
