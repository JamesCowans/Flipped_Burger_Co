# Generated by Django 4.2.11 on 2024-03-16 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_option_option_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='option_image',
            new_name='image',
        ),
    ]
