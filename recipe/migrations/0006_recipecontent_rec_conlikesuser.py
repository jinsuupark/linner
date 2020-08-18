# Generated by Django 3.1 on 2020-08-17 17:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0005_auto_20200814_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipecontent',
            name='Rec_conLikesUser',
            field=models.ManyToManyField(blank=True, related_name='rec_likes_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
