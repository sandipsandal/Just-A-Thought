# Generated by Django 3.0.9 on 2020-08-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_userdetail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='image',
            field=models.ImageField(default='default-img.png', null=True, upload_to='profile_pics'),
        ),
    ]
