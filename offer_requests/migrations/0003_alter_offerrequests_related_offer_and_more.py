# Generated by Django 4.0 on 2021-12-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_requests', '0002_offerrequests_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerrequests',
            name='related_offer',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='offerrequests',
            name='request_creator',
            field=models.CharField(max_length=20),
        ),
    ]