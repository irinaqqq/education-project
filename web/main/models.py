from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Theme(models.Model):
    title = models.CharField('Takirip', max_length=50)
    ab_theme = models.TextField('Takirip jaily')
    image = models.ImageField(upload_to='task_images', null=True, blank=True)
    classes = models.CharField('Qay synyp?', max_length=10, default="1 synyp")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

class Classes(models.Model):
    title = models.CharField('synypty engiziniz', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'классы'

class QuesModel(models.Model):
    classes = models.CharField('Qay synyp?', max_length=10, default="1 synyp")
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

class Video(models.Model):
    title = models.CharField('Taqyryp', max_length=50, null=True, blank=True, default='Tema')
    classes = models.CharField('Qay synyp?', max_length=10, default="1 synyp")
    video = EmbedVideoField('dasdsdas', null=True, blank=True)

    def __str__(self):
        return self.classes
           
    class Meta:

        verbose_name = 'видео'
        verbose_name_plural = 'видосики'

class Books(models.Model):
    title = models.CharField('Pan', max_length=50)
    authors = models.TextField('Avtorlary')
    front_image = models.ImageField(upload_to='book_images', null=True, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


        