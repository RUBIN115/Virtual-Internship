# Generated by Django 4.2 on 2023-07-02 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0023_alter_user_email_user_email_unq'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
