# Generated by Django 3.0.6 on 2020-05-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_auto_20200513_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatementmodel',
            name='transaction_id',
            field=models.CharField(default='64F1BC7B8A784094BCED5B2123FDA4DC', max_length=155),
        ),
    ]
