# Generated by Django 5.0.6 on 2024-07-05 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geolocation", "0005_universite_etudiant_delete_student_delete_university"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="etudiant",
            name="adresse",
        ),
    ]
