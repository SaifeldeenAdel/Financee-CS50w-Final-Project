# Generated by Django 3.1.6 on 2021-02-10 12:59

import api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210210_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='symbol',
            field=api.models.UpperCharField(max_length=10, unique=True),
        ),
    ]