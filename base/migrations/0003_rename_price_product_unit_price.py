# Generated by Django 5.1.2 on 2024-10-14 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
