# Generated by Django 2.2.3 on 2020-07-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200729_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
        migrations.AddField(
            model_name='content',
            name='file',
            field=models.FileField(blank=True, upload_to='documents/%Y, %m/'),
        ),
    ]
