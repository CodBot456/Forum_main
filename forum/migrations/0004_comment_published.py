# Generated by Django 4.1.1 on 2022-12-16 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_forum_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]