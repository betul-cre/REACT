# Generated by Django 4.0 on 2022-02-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='okumak için', max_length=20),
        ),
    ]
