# Generated by Django 3.0.2 on 2020-03-31 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20200331_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overall_ratings',
            name='ISBN',
            field=models.CharField(max_length=100),
        ),
    ]