# Generated by Django 2.1 on 2018-08-22 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20180822_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]