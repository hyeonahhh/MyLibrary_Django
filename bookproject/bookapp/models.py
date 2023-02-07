from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default = '')
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True, upload_to='book_photo')
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    #수업의 핵심 : 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default = '')
    
    def __str__(self):
        return self.comment