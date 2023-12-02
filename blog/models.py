from django.db import models, connection

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Blog(models.Model):
    """
    Класс для отображения блоговых записей
    """
    title = models.CharField(max_length=100, default='', verbose_name='заголовок')
    slug = models.CharField(max_length=100, default='', verbose_name='slug')
    post_content = models.TextField(**NULLABLE, verbose_name='содержимое')
    image = models.ImageField(upload_to='posts/', verbose_name='изображение', **NULLABLE)
    date_of_create = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    publication_sign = models.BooleanField(default=True, verbose_name='признак публикации')
    count_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'Название поста: {self.title}, Дата создания: {self.date_of_create}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')
