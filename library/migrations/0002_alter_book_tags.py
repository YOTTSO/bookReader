# Generated by Django 5.1.2 on 2024-11-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.CharField(max_length=250),
        ),
    ]