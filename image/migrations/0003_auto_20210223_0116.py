# Generated by Django 3.1.5 on 2021-02-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20210223_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.TextField(verbose_name={'autocomplete': 'off', 'autofocus': 'autofocus', 'size': '40', 'style': 'font-size: xx-large'}),
        ),
    ]
