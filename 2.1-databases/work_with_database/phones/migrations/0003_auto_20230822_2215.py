# Generated by Django 3.1.2 on 2023-08-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20230822_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
