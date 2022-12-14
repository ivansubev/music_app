# Generated by Django 4.1.2 on 2022-10-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='album_name',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
