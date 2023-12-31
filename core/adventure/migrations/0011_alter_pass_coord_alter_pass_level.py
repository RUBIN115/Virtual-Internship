# Generated by Django 4.2 on 2023-06-30 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0010_rename_activ_types_activity_types_pass_coord_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass',
            name='coord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.coordinate'),
        ),
        migrations.AlterField(
            model_name='pass',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.level'),
        ),
    ]
