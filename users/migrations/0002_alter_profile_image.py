# Generated by Django 3.2.9 on 2022-01-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', height_field=50, upload_to='profile_pics', width_field=50),
        ),
    ]