# Generated by Django 5.0.1 on 2024-04-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPages', '0006_newpost_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='banner',
            field=models.ImageField(default='static/images/Default_Banner.jpg', upload_to='static/Post_Banner'),
        ),
    ]
