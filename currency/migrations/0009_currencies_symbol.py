# Generated by Django 3.0.6 on 2020-05-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_auto_20200510_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencies',
            name='symbol',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
