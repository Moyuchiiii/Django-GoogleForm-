# Generated by Django 5.1.5 on 2025-01-26 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0018_page_answered_by_alter_page_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='Answered_by',
            new_name='answered_by',
        ),
    ]
