# Generated by Django 3.0.7 on 2020-08-27 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contacts',
        ),
    ]