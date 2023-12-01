# Generated by Django 4.2.4 on 2023-11-10 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Crops",
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
                ("name", models.CharField(max_length=50)),
                ("types", models.CharField(max_length=50)),
                ("total", models.IntegerField()),
                ("immersiveDate", models.DateField(auto_now_add=True, null=True)),
                ("Harvest", models.CharField(max_length=18, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Debtors",
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
                ("name", models.CharField(max_length=90)),
                ("file_no", models.CharField(max_length=50)),
                ("quantity", models.IntegerField()),
                ("farm", models.CharField(max_length=50)),
                ("amount", models.IntegerField()),
                ("signature", models.ImageField(upload_to="")),
                ("created", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Farm",
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
                ("name", models.CharField(max_length=15)),
                (
                    "description",
                    models.TextField(default="Description goes here", max_length=700),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Field",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("no_of_crops", models.CharField(blank=True, max_length=100)),
                ("crop_categories", models.CharField(blank=True, max_length=100)),
                ("location", models.TextField(blank=True, max_length=700)),
                ("about", models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="Sales",
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
                ("types", models.CharField(max_length=12)),
                ("weight", models.IntegerField()),
                ("amount", models.IntegerField()),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("created", models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TimeLine",
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
                ("number", models.IntegerField()),
                ("Field", models.CharField(max_length=2)),
                ("others", models.TextField(max_length=9000)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("image", models.ImageField(blank=True, upload_to="")),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("stipend", models.CharField(max_length=10)),
                ("mobile_number", models.CharField(max_length=11)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("edo", "Edo"),
                            ("ekiti", "Ekiti"),
                            ("kogi", "Kogi"),
                            ("kwara", "Kwara"),
                            ("lagos", "Lagos"),
                            ("ogun", "Ogun"),
                            ("ondo", "Ondo"),
                            ("osun", "Osun"),
                            ("oyo", "Oyo"),
                        ],
                        default="edo",
                        max_length=20,
                    ),
                ),
                ("country", models.CharField(default="Zimbabwe", max_length=20)),
                ("work_description", models.TextField(max_length=1000)),
                (
                    "farm",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="CropManagement.farm",
                    ),
                ),
            ],
        ),
    ]
