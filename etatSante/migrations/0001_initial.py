# Generated by Django 3.0.4 on 2020-07-05 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EtatSante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=200)),
                ('date', models.DateTimeField()),
                ('poids', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('rythmeCardiaque', models.IntegerField()),
                ('media', models.FileField(default=None, null=True, upload_to='')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='etatSante', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
