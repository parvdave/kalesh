# Generated by Django 4.2.17 on 2024-12-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masala', '0005_kalesh_kaleshi_slug_1_kalesh_kaleshi_slug_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kalesh',
            name='resolution',
            field=models.TextField(blank=True),
        ),
    ]
