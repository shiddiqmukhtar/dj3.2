# Generated by Django 3.2.9 on 2022-01-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', height_field='300', upload_to='profile_pics', width_field='300'),
        ),
    ]
