# Generated by Django 4.2.16 on 2025-03-11 10:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
