# Generated by Django 5.0.6 on 2024-07-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geolocation", "0007_alter_etudiant_code_postal_alter_etudiant_pays_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="etudiant",
            name="adresse",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
