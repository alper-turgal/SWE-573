# Generated by Django 4.0 on 2021-12-25 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer_requests', '0004_alter_offerrequests_related_offer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerrequests',
            name='related_offer',
        ),
    ]