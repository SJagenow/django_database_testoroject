# Generated by Django 5.1.1 on 2024-10-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_customer_newsletter_abo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email_adress',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]