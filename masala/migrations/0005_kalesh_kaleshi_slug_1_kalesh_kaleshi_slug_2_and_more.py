# Generated by Django 4.2.17 on 2024-12-22 06:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('masala', '0004_kalesh_response_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='kalesh',
            name='kaleshi_slug_1',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=36),
        ),
        migrations.AddField(
            model_name='kalesh',
            name='kaleshi_slug_2',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=36),
        ),
        migrations.AlterField(
            model_name='kaleshi',
            name='kaleshi_slug',
            field=models.CharField(editable=False, max_length=36, unique=True),
        ),
    ]