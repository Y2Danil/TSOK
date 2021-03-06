import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
  image = models.ImageField('Картинка', upload_to='images/', null=True, blank=True)
  rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
  create_author = models.TextField('Автор идеи', max_length=100, blank=True, null=True)
  title = models.TextField('Название статьи', max_length=48, blank=True, null=True)
  text = models.TextField('Текст статьие', blank=True, null=True)
  likes = models.IntegerField('Лайки', default=0)
  like_status = models.ManyToManyField(User, related_name='user_like', blank=True)
  created_date = models.DateTimeField(db_index=True, auto_now_add=True)
  published_date = models.DateTimeField(blank=True, null=True, db_index=True, auto_now_add=True)

  class Meta:
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'
    ordering = ['-published_date']
    
  def new_article(self):
    return self.published_date >= (timezone.now() - datetime.timedelta(days = 7))

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  author = models.CharField('Автор комментария', max_length=60)
  comment_text = models.TextField('Текст комметария', max_length=500)
  pub_date = models.DateTimeField('Дата публикации', db_index=True, auto_now_add=True)

  class Meta:
    verbose_name = 'Комментарий'
    verbose_name_plural = 'Комментарии'

  def __str__(self):
    return self.author
  
class Rubric(models.Model):
  name = models.TextField('Название', max_length=30, db_index=True, unique=True)
  
  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'Рубрики'
    verbose_name = 'Рубрика'
    ordering = ['name']