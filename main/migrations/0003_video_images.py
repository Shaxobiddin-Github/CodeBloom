# Generated by Django 5.1.5 on 2025-01-27 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='video_images'),
        ),
    ]
