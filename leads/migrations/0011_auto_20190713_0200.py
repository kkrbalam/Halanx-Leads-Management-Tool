# Generated by Django 2.2 on 2019-07-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_remove_leadstatuscategory_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseownerleadactivity',
            name='acknowledged_by_affiliate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tenantleadactivity',
            name='acknowledged_by_affiliate',
            field=models.BooleanField(default=False),
        ),
    ]