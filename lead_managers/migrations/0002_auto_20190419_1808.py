# Generated by Django 2.2 on 2019-04-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead_managers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadmanager',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]