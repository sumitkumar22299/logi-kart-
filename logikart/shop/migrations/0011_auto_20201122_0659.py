# Generated by Django 3.1.3 on 2020-11-22 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]
