# Generated by Django 2.1 on 2018-08-19 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Answer',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='choice_text',
            new_name='answer',
        ),
    ]
