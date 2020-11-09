# Generated by Django 3.1.2 on 2020-11-09 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accessible_restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="approvalpendingusers",
            name="auth_status",
            field=models.CharField(
                choices=[
                    ("approve", "Approve"),
                    ("pending", "Pending"),
                    ("disapprove", "Disapprove"),
                ],
                default="N/A",
                max_length=16,
            ),
        ),
    ]
