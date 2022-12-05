from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Quote(models.Model):
    class Genre(models.TextChoices):
        General = "General","General"
        Love = "Love","Love"
        Economy = "Economy","Economy"
        Education = "Education","Education"
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    quoted_by = models.CharField(max_length=100, null=False,blank=True)
    image = models.ImageField(null=True, blank=True, default='/anonymous.jpeg')
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length = 50, null=False,default=Genre.General, choices=Genre.choices)
    description = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title
    

