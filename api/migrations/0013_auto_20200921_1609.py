# Generated by Django 3.0 on 2020-09-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_workout_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
