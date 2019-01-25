from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntegerField()

    # __ : 내부에서 쓰기 위한 용도
    # calss 내의 함수는 항상 self를 적어줘야함
    def __str__(self):
        return "{} ({})".format(self.title, self.view_count)

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=100)
