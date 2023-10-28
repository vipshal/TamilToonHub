# Generated by Django 4.2.5 on 2023-10-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0005_alter_video_image_alter_video_movie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.FileField(blank=True, upload_to='CategoryImage/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.FileField(blank=True, upload_to='FrontImage/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='movie',
            field=models.FileField(upload_to='video/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='poster',
            field=models.FileField(blank=True, upload_to='poster/'),
        ),
    ]
