# Generated by Django 3.2.5 on 2022-06-13 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applemusicsite2', '0002_register_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='firstName',
            new_name='firstname',
        ),
    ]
