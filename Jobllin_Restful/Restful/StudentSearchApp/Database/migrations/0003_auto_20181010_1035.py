# Generated by Django 2.1.2 on 2018-10-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0002_auto_20181010_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='st_roll',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
