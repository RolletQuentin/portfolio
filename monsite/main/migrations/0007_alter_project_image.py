# Generated by Django 4.1.2 on 2022-10-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(default="images/default.svg", upload_to=""),
        ),
    ]
