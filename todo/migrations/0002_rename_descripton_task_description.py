# Generated by Django 4.1.5 on 2023-01-18 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descripton',
            new_name='description',
        ),
    ]
