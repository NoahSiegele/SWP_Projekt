# Generated by Django 2.1.5 on 2019-03-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noten', '0006_auto_20190314_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='type',
            field=models.CharField(default='', max_length=150),
        ),
    ]
