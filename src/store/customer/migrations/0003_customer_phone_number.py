# Generated by Django 5.0.2 on 2024-05-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_alter_customer_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="phone_number",
            field=models.CharField(default="", max_length=12),
            preserve_default=False,
        ),
    ]
