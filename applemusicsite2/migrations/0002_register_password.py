# Generated by Django 3.2.5 on 2022-06-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applemusicsite2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default='null', max_length=80),
            preserve_default=False,
        ),
    ]