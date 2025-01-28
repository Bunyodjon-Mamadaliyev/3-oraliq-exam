# Generated by Django 5.1.5 on 2025-01-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
