# Generated by Django 2.1 on 2018-08-27 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0011_question_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
    ]
