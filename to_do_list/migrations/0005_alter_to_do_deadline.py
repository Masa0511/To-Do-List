# Generated by Django 4.0.2 on 2022-03-29 06:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0004_alter_to_do_deadline_alter_to_do_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
