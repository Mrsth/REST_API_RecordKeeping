# Generated by Django 3.1.5 on 2021-01-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaseItem', models.CharField(max_length=30)),
                ('purchaseAmount', models.IntegerField()),
                ('purchaseDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesItem', models.CharField(max_length=30)),
                ('salesAmount', models.IntegerField()),
                ('salesDate', models.DateField()),
            ],
        ),
    ]
