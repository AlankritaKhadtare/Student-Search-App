# Generated by Django 2.1.2 on 2018-10-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0004_auto_20181010_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='st_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
