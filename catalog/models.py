from django.db import models
from django.db import connection

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Category(models.Model):
    """
    Модель для отображения таблицы Категории в БД
    """
    name_category = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        """
        Строковое отображение объекта
        :return:
        """
        return f'{self.name_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Product(models.Model):
    """
    Модель для отображения таблицы Продукты в БД
    """
    name_product = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_making = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_changing = models.DateTimeField(auto_now_add=True, verbose_name='дата последнег оизменения')

    def __str__(self):
        """
        Строковое отображение объекта
        :return:
        """
        return f'{self.name_product} {self.category} {self.price} {self.date_making}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')