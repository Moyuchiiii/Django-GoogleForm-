# Generated by Django 5.1.5 on 2025-01-26 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_page_pucture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='pucture',
            new_name='picture',
        ),
    ]
