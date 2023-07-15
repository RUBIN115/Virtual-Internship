# Generated by Django 4.2 on 2023-06-29 16:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+799999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')])),
                ('middle_name', models.CharField(max_length=100, verbose_name='Middlename')),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beautyTitle', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('other_titles', models.CharField(max_length=30)),
                ('connect', models.CharField(max_length=30, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(max_length=10, null=True, verbose_name='Winter')),
                ('summer', models.CharField(max_length=10, null=True, verbose_name='Summer')),
                ('autumn', models.CharField(max_length=10, null=True, verbose_name='Autumn')),
                ('spring', models.CharField(max_length=10, null=True, verbose_name='Spring')),
                ('pass_to_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.pass')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('image_to_pass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.pass')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitude')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('coords_to_pass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.pass')),
            ],
        ),
    ]
