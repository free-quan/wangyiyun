# Generated by Django 3.0.8 on 2020-08-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='head_link',
            field=models.CharField(default='', max_length=50, verbose_name='头像链接'),
        ),
    ]
