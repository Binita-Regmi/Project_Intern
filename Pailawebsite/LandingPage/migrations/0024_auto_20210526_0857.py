# Generated by Django 2.2 on 2021-05-26 03:12

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0023_auto_20210526_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media_sliding',
            name='know_more_hyperlink',
            field=embed_video.fields.EmbedVideoField(blank=True, max_length=500, null=True),
        ),
    ]
