# Generated by Django 2.2 on 2021-05-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aboutpage', '0004_auto_20210526_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_progress',
            name='is_available',
            field=models.BooleanField(max_length=400),
        ),
        migrations.AlterField(
            model_name='company_progress',
            name='title',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
