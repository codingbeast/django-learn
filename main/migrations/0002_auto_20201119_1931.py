# Generated by Django 3.1.1 on 2020-11-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]