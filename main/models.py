from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=221)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=221)
    category = models.CharField(max_length=221)
    image = models.ImageField(upload_to="article_images/", blank=True)

    def __str__(self):
        return self.title

class Email(models.Model):
    mail = models.EmailField(max_length=221)
    
    def __str__(self):
        return self.mail
