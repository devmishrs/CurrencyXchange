# Generated by Django 3.0.6 on 2020-05-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0004_auto_20200513_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatementmodel',
            name='transaction_id',
            field=models.CharField(default='FBD1169C0EC9483EABB6234F270E5C78', max_length=155),
        ),
    ]
