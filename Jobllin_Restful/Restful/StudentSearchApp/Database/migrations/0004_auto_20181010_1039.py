# Generated by Django 2.1.2 on 2018-10-10 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0003_auto_20181010_1035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('st_roll',)},
        ),
    ]