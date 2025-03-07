# Generated by Django 5.1.6 on 2025-02-18 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0002_alter_purchase_balance_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Denomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(unique=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='available_stocks',
            new_name='available_stock',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='timestamp',
            new_name='purchase_date',
        ),
        migrations.RenameField(
            model_name='purchaseitem',
            old_name='subtotal',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='balance_amount',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='paid_amount',
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='tax',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total_amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='billapp.customer'),
            preserve_default=False,
        ),
    ]
