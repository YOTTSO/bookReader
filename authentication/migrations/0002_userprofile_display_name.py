# Generated by Django 5.1.2 on 2024-11-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(default='Anonim', max_length=255),
            preserve_default=False,
        ),
    ]
