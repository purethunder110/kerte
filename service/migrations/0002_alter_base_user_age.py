# Generated by Django 5.0.1 on 2024-02-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_user',
            name='Age',
            field=models.IntegerField(null=True),
        ),
    ]