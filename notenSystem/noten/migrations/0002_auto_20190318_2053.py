# Generated by Django 2.1.7 on 2019-03-18 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noten', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name_plural': 'Noten'},
        ),
        migrations.AlterModelOptions(
            name='prüfung',
            options={'verbose_name_plural': 'Prüfungen'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name_plural': 'Teste'},
        ),
        migrations.AlterModelOptions(
            name='unterricht',
            options={'verbose_name_plural': 'Unterrichte'},
        ),
    ]