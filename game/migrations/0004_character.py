# Generated by Django 4.2 on 2023-11-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0003_remove_chatmessage_game_session_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
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
                ("description", models.TextField()),
                ("quality_1_choices", models.CharField(max_length=255)),
                ("quality_2_choices", models.CharField(max_length=255)),
                ("quality_3_choices", models.CharField(max_length=255)),
                ("interest_1_choices", models.CharField(max_length=255)),
                ("interest_2_choices", models.CharField(max_length=255)),
                ("interest_3_choices", models.CharField(max_length=255)),
                ("activity_1_choices", models.CharField(max_length=255)),
                ("activity_2_choices", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="characters/"),
                ),
            ],
        ),
    ]
