# Generated by Django 3.0.7 on 2020-06-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog site', max_length=230),
        ),
    ]