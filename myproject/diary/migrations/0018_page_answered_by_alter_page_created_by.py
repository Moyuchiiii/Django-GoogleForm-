# Generated by Django 5.1.5 on 2025-01-26 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0017_alter_page_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='Answered_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answered_pages', to=settings.AUTH_USER_MODEL, verbose_name='回答者'),
        ),
        migrations.AlterField(
            model_name='page',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_pages', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
    ]
