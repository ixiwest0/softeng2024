# Generated by Django 4.1 on 2024-11-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_head_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="file_upload",
            field=models.FileField(blank=True, upload_to="blog/files/%Y/%m/%d/"),
        ),
    ]
