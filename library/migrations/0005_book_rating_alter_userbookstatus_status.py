# Generated by Django 5.1.2 on 2024-12-16 16:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_tag_remove_book_tags_book_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0.0, help_text='Рейтинг книги от 0 до 5', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='userbookstatus',
            name='status',
            field=models.CharField(choices=[('reading', 'Читаю'), ('completed', 'Прочитано'), ('planned', 'Запланировано'), ('abandoned', 'Заброшено'), ('favorite', 'Избранное')], max_length=10),
        ),
    ]