# Generated by Django 2.1 on 2018-08-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_answer_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=400),
        ),
    ]