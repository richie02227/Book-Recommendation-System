# Generated by Django 3.0.2 on 2020-01-27 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0003_auto_20200127_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='books',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
