# Generated by Django 3.1.6 on 2021-02-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210210_2124'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='watchlist',
            constraint=models.UniqueConstraint(fields=('user', 'symbol'), name='user_symbol'),
        ),
    ]
