# Generated by Django 3.2.6 on 2021-08-18 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_message_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='ContactForm',
        ),
    ]
