# Generated by Django 3.0.2 on 2020-01-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0002_auto_20200116_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='ISBN',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='ISBN',
            field=models.CharField(max_length=100),
        ),
    ]
