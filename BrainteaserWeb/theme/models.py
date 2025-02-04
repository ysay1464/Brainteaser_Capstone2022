from django.db import models
from datetime import date
# Create your models here.

class Board(models.Model):
    TeaserID = models.IntegerField(verbose_name="번호", primary_key=True)
    Title = models.CharField(max_length=50, verbose_name="제목")
    Category = models.CharField(max_length=15)
    AccID = models.CharField(max_length=15, verbose_name="작성자")
    Date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    Clicked = models.IntegerField(verbose_name="조회수")

    class Meta:
        db_table = 'brainTeaser'
        managed = False

    def __str__(self):
        return '{},{},{},{},{}'.format(self.TeaserID,self.Title,self.AccID,self.Date.date(),self.Clicked)


class BoardContents(models.Model):
    TeaserID = models.IntegerField(verbose_name="번호", primary_key=True)
    Title = models.CharField(max_length=50, verbose_name="제목")
    Teaser = models.TextField(verbose_name="본문")
    AccID = models.CharField(max_length=15, verbose_name="작성자")
    Date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    Clicked = models.IntegerField(verbose_name="조회수")

    class Meta:
        db_table = 'brainTeaser'
        managed = False

    def __str__(self):
        return '{},{},{},{},{},{}'.format(self.Title,self.TeaserID,self.AccID,self.Date.date(),self.Clicked,self.Teaser)