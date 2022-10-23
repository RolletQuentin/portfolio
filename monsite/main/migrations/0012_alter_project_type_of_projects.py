# Generated by Django 4.1.2 on 2022-10-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_remove_project_image_project_image_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="type_of_projects",
            field=models.CharField(
                choices=[
                    ("Web", "Web"),
                    ("Python", "Python"),
                    ("C", "C"),
                    ("Java", "Java"),
                    ("A venir", "Next"),
                ],
                default="Web",
                max_length=10,
            ),
        ),
    ]