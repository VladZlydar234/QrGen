# Generated by Django 4.1.5 on 2023-06-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0006_remove_littleimage_image_little_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='littleimage',
            name='image_little',
            field=models.ImageField(default=0, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userimage',
            name='image_bg',
            field=models.ImageField(default=0, upload_to='media/'),
            preserve_default=False,
        ),
    ]