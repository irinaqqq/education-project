# Generated by Django 4.0.4 on 2022-05-23 06:42

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_video_options_remove_video_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='classes',
            field=models.CharField(default='1 synyp', max_length=10, verbose_name='Qay synyp?'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]