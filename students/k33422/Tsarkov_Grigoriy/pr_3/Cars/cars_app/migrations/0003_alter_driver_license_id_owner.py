# Generated by Django 4.1.3 on 2022-11-26 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cars_app", "0002_alter_car_owner_options_alter_car_owner_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver_license",
            name="id_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="license_owner",
                to="cars_app.car_owner",
            ),
        ),
    ]