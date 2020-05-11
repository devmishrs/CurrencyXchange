import sys
from django.db import models
from django.contrib.auth.models import User
from currency.models import UserWallet

# Create your models here.

class MoneyTransferLog(models.Model):
    from_wallet = models.ForeignKey(UserWallet, on_delete=models.CASCADE, related_name='from_wallet')
    to_wallet = models.ForeignKey(UserWallet, on_delete=models.CASCADE, related_name='to_wallet')
    amount = models.FloatField(default=0.0)
    transfer_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'money_transfer_log'
