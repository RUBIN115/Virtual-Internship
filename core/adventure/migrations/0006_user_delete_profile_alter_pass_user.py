# Generated by Django 4.2 on 2023-06-30 18:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0005_alter_activity_types_title_alter_areas_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+799999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AlterField(
            model_name='pass',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.user'),
        ),
    ]
