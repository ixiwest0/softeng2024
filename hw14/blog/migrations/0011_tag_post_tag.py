# Generated by Django 4.1 on 2024-11-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_alter_category_options_alter_post_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=200, unique=True),
                ),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(blank=True, null=True, to="blog.tag"),
        ),
    ]
