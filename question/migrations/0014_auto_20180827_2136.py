# Generated by Django 2.1 on 2018-08-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0013_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(max_length=40),
        ),
    ]
