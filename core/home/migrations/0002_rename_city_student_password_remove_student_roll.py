# Generated by Django 5.1.7 on 2025-03-26 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='city',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
    ]
