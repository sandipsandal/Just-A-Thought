# Generated by Django 3.0.9 on 2020-08-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_addpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
