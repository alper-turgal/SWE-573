# Generated by Django 4.0 on 2022-01-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0007_serviceoffer_service_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceoffer',
            name='service_comment',
            field=models.CharField(max_length=200, verbose_name='Yorumunuz'),
        ),
    ]
