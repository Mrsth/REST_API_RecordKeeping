# Generated by Django 3.1.5 on 2021-02-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis1', '0012_purchaserequisitiontableacceptreject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequisitiontableacceptreject',
            name='PurchaseRequisitionTable_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value', to='apis1.purchaserequisitiontable'),
        ),
    ]
