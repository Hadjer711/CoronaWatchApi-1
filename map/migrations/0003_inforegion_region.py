# Generated by Django 3.0.4 on 2020-06-03 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20200603_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='inforegion',
            name='region',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='map.Region'),
        ),
    ]
