# Generated by Django 3.1.13 on 2023-03-10 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_calculation_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculation',
            old_name='question',
            new_name='expression',
        ),
    ]
