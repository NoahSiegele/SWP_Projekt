# Generated by Django 2.1.5 on 2019-03-14 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noten', '0003_auto_20190314_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prüfungstyp',
            options={'verbose_name_plural': 'Prüfungstyp'},
        ),
        migrations.AddField(
            model_name='note',
            name='Prüfungstyp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='noten.Prüfungstyp'),
        ),
    ]