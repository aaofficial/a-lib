# Generated by Django 4.2.3 on 2023-07-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oflib", "0003_delete_books"),
    ]

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("adddate", models.DateField()),
            ],
        ),
    ]
