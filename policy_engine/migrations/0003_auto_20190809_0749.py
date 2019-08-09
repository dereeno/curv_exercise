# Generated by Django 2.2.4 on 2019-08-09 07:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_engine', '0002_auto_20190809_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='currency',
            field=models.CharField(choices=[('BTC', 'BTC'), ('USD', 'USD'), ('AUD', 'AUD'), ('BRL', 'BRL'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('DKK', 'DKK'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('HKD', 'HKD'), ('INR', 'INR'), ('ISK', 'ISK'), ('JPY', 'JPY'), ('KRW', 'KRW'), ('NZD', 'NZD'), ('PLN', 'PLN'), ('RUB', 'RUB'), ('SEK', 'SEK'), ('SGD', 'SGD'), ('THB', 'THB'), ('TWD', 'TWD')], max_length=3),
        ),
        migrations.AlterField(
            model_name='rule',
            name='max_amount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]