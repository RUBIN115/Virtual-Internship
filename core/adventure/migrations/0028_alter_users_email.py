# Generated by Django 4.2 on 2023-07-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0027_users_remove_perevaluser_user_ptr_users_email_unq_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
