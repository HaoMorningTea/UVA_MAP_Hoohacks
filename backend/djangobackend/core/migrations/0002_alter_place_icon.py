# Generated by Django 5.0.3 on 2024-03-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
    ]