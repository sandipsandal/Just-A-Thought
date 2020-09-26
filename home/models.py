from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    mobile= models.CharField(max_length = 13, null=True)
    image = models.ImageField(default="default.png", upload_to='profile_pics')

    def __str__(self):
        return self.user.username 

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 13)
    email = models.CharField(max_length = 100)
    content = RichTextField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from : ' + self.name + ' - ' + self.email

# class AddPost(models.Model):
#     sno = models.AutoField(primary_key=True)
#     title = models.CharField(max_length = 255)
#     content = models.TextField()
#     author = models.CharField(max_length = 13)
#     timeStamp = models.DateTimeField(default = now)

#     def __str__(self):
#         return 'Post posted by :' + self.title + ' by ' + self.author


