# Generated by Django 5.1.6 on 2025-02-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='balance_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='paid_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total_amount',
            field=models.FloatField(null=True),
        ),
    ]
