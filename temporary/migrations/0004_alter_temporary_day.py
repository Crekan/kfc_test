# Generated by Django 4.2 on 2023-05-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporary', '0003_temporary_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporary',
            name='day',
            field=models.CharField(choices=[('Понедельник', 'mon'), ('tue', 'Вторник'), ('wed', 'Среда'), ('thu', 'Четверг'), ('fri', 'Пятница'), ('sat', 'Суббота'), ('sun', 'Восересенье')], max_length=20),
        ),
    ]
