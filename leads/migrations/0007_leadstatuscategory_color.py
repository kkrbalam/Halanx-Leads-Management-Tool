# Generated by Django 2.2 on 2019-04-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_auto_20190416_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadstatuscategory',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]