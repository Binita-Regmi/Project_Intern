# Generated by Django 2.2 on 2021-05-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0005_quantity_title_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity_title',
            name='quantity',
            field=models.IntegerField(default=True),
        ),
    ]
