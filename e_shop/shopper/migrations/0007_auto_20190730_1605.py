# Generated by Django 2.2.1 on 2019-07-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0006_auto_20190730_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vat',
            field=models.FloatField(choices=[(0.23, '23%'), (0.08, '8%'), (0.05, '5%'), (0, '0%')], default=0.23),
        ),
    ]
