# Generated by Django 2.2 on 2021-05-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0024_auto_20210526_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media_sliding',
            old_name='know_more_hyperlink',
            new_name='know_more_hyperlink_vedios',
        ),
        migrations.AddField(
            model_name='media_sliding',
            name='know_more_hyperlink_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
