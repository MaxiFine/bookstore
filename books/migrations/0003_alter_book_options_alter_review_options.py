# Generated by Django 4.1.5 on 2023-01-27 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_review_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={},
        ),
    ]
