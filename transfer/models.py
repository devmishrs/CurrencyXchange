import uuid
from django.db import models
from django.contrib.auth.models import User
from currency.models import UserWallet, ForeignCurrencyWallet, TransactionMethod

# Create your models here.

class OrderStatementModel(models.Model):
    """  UserWallet => ForeignCurrencyWallet
         UserWallet(self) => UserWallet(other)
    """
    transaction_id = models.CharField(max_length=155, default=uuid.uuid4().hex.upper())
    timestamp = models.DateTimeField(auto_now_add=True)
    to_self = models.BooleanField(default=False)
    method = models.ForeignKey(TransactionMethod, on_delete=models.SET_NULL, null=True)         ## TransactionMethod  
    transaction_amount = models.FloatField(default=0.0)
    from_wallet = models.ForeignKey(UserWallet, on_delete=models.SET_NULL, null=True, related_name='from_wallet')   ## from UserWallet
    to_wallet = models.ForeignKey(UserWallet, on_delete=models.SET_NULL, null=True, related_name='to_wallet')     ## to UserWallet
    is_foreingn = models.BooleanField(default=False)
    to_foreign_wallet = models.ForeignKey(ForeignCurrencyWallet, on_delete=models.SET_NULL,
                                          null=True, related_name='to_foreign_wallet')       ## to ForeignWallet
    is_success = models.BooleanField(default=False)

    class Meta:
        db_table = 'order_statement_model'

    def __str__(self):
        return self.transaction_id
