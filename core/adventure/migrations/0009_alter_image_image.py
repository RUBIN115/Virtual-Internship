# Generated by Django 4.2 on 2023-06-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0008_image_rename_activity_types_activ_types_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]