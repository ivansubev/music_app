# Generated by Django 4.1.2 on 2022-10-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_exampletwothreefour_delete_exampletwothree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exampletwothreefour',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='exampletwothreefour',
            name='last_name',
        ),
        migrations.AddField(
            model_name='exampletwothreefour',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]