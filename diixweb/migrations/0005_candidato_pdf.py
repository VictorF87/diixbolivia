# Generated by Django 3.1.2 on 2020-10-09 07:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diixweb', '0004_auto_20201009_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='pdf',
            field=models.FileField(default=datetime.datetime(2020, 10, 9, 7, 52, 46, 76649, tzinfo=utc), upload_to='pdf/candidatos', verbose_name='Plan de Gobierno'),
            preserve_default=False,
        ),
    ]
