# Generated by Django 4.1.5 on 2023-01-27 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]