# Generated by Django 4.2.5 on 2023-10-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievanceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievanceform',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
