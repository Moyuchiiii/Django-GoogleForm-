# Generated by Django 5.1.5 on 2025-01-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_alter_page_q10_alter_page_q2_alter_page_q3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='Answertf',
            field=models.BooleanField(default=False, verbose_name='回答'),
        ),
    ]
