from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', verbose_name='Пользователи системы')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    friends = models.ManyToManyField(User, related_name='friend', null=True, blank=True, verbose_name='Друзья')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фотография')


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголок")
    text = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(User, related_name='author', verbose_name='Автор поста', on_delete=models.PROTECT)


    def __str__(self):
        return "%s - %s" % (self.title, self.author)