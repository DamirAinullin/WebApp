# Generated by Django 2.1.3 on 2018-12-04 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='added_ad',
            new_name='added_at',
        ),
    ]
