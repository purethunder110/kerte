# Generated by Django 5.0.1 on 2024-02-13 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LandingPages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newpost',
            name='Community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='LandingPages.community'),
        ),
        migrations.AddField(
            model_name='newpost',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tags',
            name='Community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LandingPages.community'),
        ),
        migrations.AddField(
            model_name='newpost',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='LandingPages.tags'),
        ),
    ]
