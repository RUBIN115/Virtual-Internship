# Generated by Django 4.2 on 2023-07-01 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0013_alter_image_image_alter_image_image_to_pass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('other_titles', models.CharField(max_length=30)),
                ('connect', models.CharField(max_length=30, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=8)),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.coordinate')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_to_pass',
        ),
        migrations.DeleteModel(
            name='Pass',
        ),
        migrations.AddField(
            model_name='pereval',
            name='images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.image'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.level'),
        ),
        migrations.AddField(
            model_name='pereval',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.user'),
        ),
    ]
