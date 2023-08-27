# Generated by Django 3.1.2 on 2023-08-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20230827_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.Teacher', verbose_name='Учитель'),
        ),
    ]
