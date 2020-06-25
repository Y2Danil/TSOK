# Generated by Django 3.0.5 on 2020-06-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Top', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_author',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Автор идеи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Название статьи'),
        ),
    ]