# Generated by Django 3.1.5 on 2021-01-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis1', '0005_auto_20210129_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasetable',
            name='purchaseDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]