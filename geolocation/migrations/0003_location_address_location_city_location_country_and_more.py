# Generated by Django 5.0.6 on 2024-07-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geolocation", "0002_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="location",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="location",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="location",
            name="postal_code",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]