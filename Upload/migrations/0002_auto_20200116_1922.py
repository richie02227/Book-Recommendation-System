# Generated by Django 3.0.2 on 2020-01-16 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='BookRating',
            new_name='Book_Rating',
        ),
        migrations.AlterField(
            model_name='ratings',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Upload.Books'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Upload.Users'),
        ),
    ]
