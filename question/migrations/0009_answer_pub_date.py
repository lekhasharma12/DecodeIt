# Generated by Django 2.1 on 2018-08-23 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0008_auto_20180823_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
