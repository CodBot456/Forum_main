# Generated by Django 4.1.1 on 2022-12-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_commnet_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='body',
            field=models.TextField(null=True),
        ),
    ]