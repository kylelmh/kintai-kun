# Generated by Django 3.2.13 on 2022-04-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kintai_kun', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='worktimestamp',
            name='unique_stamp_date',
        ),
        migrations.AddConstraint(
            model_name='worktimestamp',
            constraint=models.UniqueConstraint(fields=('employee', 'date', 'stamp_type'), name='unique_stamp_date'),
        ),
    ]