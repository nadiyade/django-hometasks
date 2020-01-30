from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date, time, timedelta


GENDER = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
    ('Unknown', 'Unknown')
)


class MyUser(AbstractUser):
    purse = models.DecimalField(default=10000.00, max_digits=7, decimal_places=2, verbose_name="Кошелёк")
    birthday = models.DateTimeField(verbose_name="Дата рождения", default=datetime.now()-timedelta(days=10957.5))
    gender = models.CharField(choices=GENDER, max_length=10, default='Unknown')

    def __str__(self):
        return "Пользователь {}".format(self.username)


class Tovar(models.Model):
    name = models.CharField(max_length=5000, default="Название товара", verbose_name="Название")
    description = models.TextField(default="Описание товара", verbose_name="Описание")
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name="Цена товара")
    number = models.PositiveSmallIntegerField(default=0, verbose_name="Количество на складе")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "Товар {}, pk {}, цена {} грн.".format(self.name, self.pk, self.price)


class Purchase(models.Model):
    buyer = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, verbose_name="Покупатель", default=None)
    article = models.ForeignKey(to=Tovar, on_delete=models.DO_NOTHING, verbose_name="Товар", default=None)
    article_number = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    purchase_date = models.DateTimeField(verbose_name="Дата и время покупки", auto_now_add=True)


class Vozvrat(models.Model):
    item = models.ForeignKey(to=Purchase, on_delete=models.CASCADE, verbose_name="Товар к возврату", default=None)
    request_time = models.DateTimeField(verbose_name="Дата запроса", auto_now_add=True)

    def __str__(self):
        return "Товар {} возвращает покупатель {}".format(self.item.article.name, self.item.buyer.username)


