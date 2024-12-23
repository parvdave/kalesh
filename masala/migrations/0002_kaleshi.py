# Generated by Django 4.2.17 on 2024-12-22 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kaleshi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kaleshi_name', models.CharField(default='TBA', max_length=100)),
                ('kaleshi_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kalesh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masala.kalesh')),
            ],
        ),
    ]
