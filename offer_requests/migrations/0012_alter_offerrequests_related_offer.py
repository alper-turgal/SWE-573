# Generated by Django 4.0 on 2022-01-02 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0009_alter_serviceoffer_service_comment'),
        ('offer_requests', '0011_alter_offerrequests_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerrequests',
            name='related_offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='offers.serviceoffer'),
        ),
    ]