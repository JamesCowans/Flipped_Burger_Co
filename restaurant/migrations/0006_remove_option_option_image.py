# Generated by Django 4.2.11 on 2024-03-16 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_option_image_option_option_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='option_image',
        ),
    ]
