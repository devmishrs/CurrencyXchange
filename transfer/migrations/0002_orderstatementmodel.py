# Generated by Django 3.0.6 on 2020-05-12 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0012_auto_20200512_0510'),
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatementModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(default='67167EF2546A4ACA98C03D493DCB1DBB', max_length=155)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('to_self', models.BooleanField(default=False)),
                ('transaction_amount', models.FloatField(default=0.0)),
                ('is_foreingn', models.BooleanField(default=False)),
                ('is_success', models.BooleanField(default=False)),
                ('from_wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_wallet', to='currency.UserWallet')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.TransactionMethod')),
                ('to_foreign_wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_foreign_wallet', to='currency.ForeignCurrencyWallet')),
                ('to_wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_wallet', to='currency.UserWallet')),
            ],
            options={
                'db_table': 'order_statement_model',
            },
        ),
    ]
