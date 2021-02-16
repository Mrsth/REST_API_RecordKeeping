# Generated by Django 3.1.5 on 2021-02-14 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis1', '0011_auto_20210212_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseRequisitionTableAcceptReject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.BooleanField(default=False)),
                ('PurchaseRequisitionTable_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis1.purchaserequisitiontable')),
            ],
        ),
    ]
