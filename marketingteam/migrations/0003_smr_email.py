# Generated by Django 2.0.2 on 2018-05-30 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketingteam', '0002_auto_20180530_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='smr',
            name='email',
            field=models.EmailField(max_length=256, null=True),
        ),
    ]
