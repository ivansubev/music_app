# Generated by Django 4.1.2 on 2022-10-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_exampletwothreefour_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
