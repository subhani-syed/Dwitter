# Generated by Django 4.0.5 on 2022-07-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_userfollowing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=100, null=True, verbose_name='bio'),
        ),
    ]
