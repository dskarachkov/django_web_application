# Generated by Django 5.0.4 on 2024-04-09 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_rename_topic_topiiic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topiiic',
            new_name='Topic',
        ),
    ]
