# Generated by Django 4.0.4 on 2022-04-27 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth1', '0002_alter_user_data_email_alter_user_data_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_data',
            old_name='name',
            new_name='username',
        ),
    ]
