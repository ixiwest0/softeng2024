# Generated by Django 4.1 on 2024-11-29 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_tag_post_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(blank=True, to="blog.tag"),
        ),
    ]