from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Appointment(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(max_length=200)

    messsage = models.TextField()


    def __str__(self):
        return f'{self.client_name}: {self.messsage}'




class Category(models.Model):
    name = models.CharField(max_length=100)
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed_categories = models.ManyToManyField(Category)
    pass

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)







