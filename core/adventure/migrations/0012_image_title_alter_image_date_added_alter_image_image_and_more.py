# Generated by Django 4.2 on 2023-06-30 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0011_alter_pass_coord_alter_pass_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_to_pass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.pass'),
        ),
    ]