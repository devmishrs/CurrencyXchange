from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.encoding import uri_to_iri


# Create your models here.

class Currencies(models.Model):
    currency = models.CharField(max_length=20)
    currency_code = models.CharField(max_length=8)
    symbol = models.CharField(max_length=12, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.currency_code

    class Meta:
        db_table = 'currency'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='image')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile'




class UserWalletManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__is_active=True)

class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_balance = models.FloatField(default=0.0)
    currency_type = models.ForeignKey(Currencies, on_delete=models.CASCADE, default=1)
    update_time = models.DateTimeField(auto_now_add=True)

    objects = UserWalletManager()

    class Meta:
        db_table = 'user_wallet'

    def __str__(self):
        return self.user.username




class ForeignCurrencyWalletManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__is_active=True)

class ForeignCurrencyWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, default=1)
    update_time = models.DateTimeField(auto_now_add=True)

    objects = ForeignCurrencyWalletManager()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'foreign_currency_wallet'

def create_user_profile(sender, instance, created, **kwargs):
    print('Called Profile model')
    if created:
        UserProfile.objects.create(user=instance)
        UserWallet.objects.create(user=instance, wallet_balance=0.0)

post_save.connect(create_user_profile, sender=User)
