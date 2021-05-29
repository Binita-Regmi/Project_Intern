# Generated by Django 2.2 on 2021-05-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlidingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('Button', models.TextField(blank=True, max_length=200)),
                ('Image', models.ImageField(upload_to='photos/home')),
            ],
        ),
    ]
