# Generated by Django 3.1.5 on 2021-01-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_auto_20210111_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_table',
            name='purchase_amount',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchase_table',
            name='purchase_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='sales_table',
            name='sales_amount',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='sales_table',
            name='sales_date',
            field=models.CharField(max_length=10),
        ),
    ]
