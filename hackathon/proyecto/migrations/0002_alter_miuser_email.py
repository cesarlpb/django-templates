# Generated by Django 5.0.6 on 2024-06-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proyecto", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="miuser",
            name="email",
            field=models.EmailField(max_length=100),
        ),
    ]
