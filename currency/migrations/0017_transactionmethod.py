# Generated by Django 3.0.6 on 2020-05-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0016_delete_transactionmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'trancaction_method',
            },
        ),
    ]
