from django.db import models, connection


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите название категории продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену за покупку"
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        blank=True,
        null=True,
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        blank=True,
        null=True,
        help_text="Укажите дату последнего изменения",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0

    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    slug = models.CharField(
        max_length=150,
        verbose_name='slug',
        null=True,
        blank=True
    )
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="product",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Продукт",
    )

    number = models.PositiveIntegerField(
        verbose_name="Номер версии"

    )

    name = models.CharField(
        max_length=150,
        verbose_name="Название версии"
    )

    is_active = models.BooleanField(
        verbose_name="Признак текущей версии"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.number} - {self.name}"

