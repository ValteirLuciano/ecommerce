# Generated by Django 2.2.9 on 2021-05-08 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210506_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug padrao'),
            preserve_default=False,
        ),
    ]