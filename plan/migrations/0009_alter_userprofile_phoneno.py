# Generated by Django 3.2.6 on 2021-08-12 12:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0008_auto_20210812_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phoneno',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]