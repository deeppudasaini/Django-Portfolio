# Generated by Django 2.2.13 on 2021-05-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.IntegerField(),
        ),
    ]
