# Generated by Django 4.2 on 2023-06-30 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0006_user_delete_profile_alter_pass_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pass',
            old_name='beautyTitle',
            new_name='beauty_title',
        ),
    ]
