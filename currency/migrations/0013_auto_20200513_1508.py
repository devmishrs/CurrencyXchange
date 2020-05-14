# Generated by Django 3.0.6 on 2020-05-13 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0012_auto_20200512_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=22)),
            ],
            options={
                'db_table': 'trancaction_method',
            },
        ),
        migrations.AddField(
            model_name='foreigncurrencywallet',
            name='method',
            field=models.ForeignKey(default='CREDIT', on_delete=django.db.models.deletion.CASCADE, to='currency.TransactionMethod'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userwallet',
            name='method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='currency.TransactionMethod'),
            preserve_default=False,
        ),
    ]
