# Generated by Django 3.1.2 on 2020-10-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diixweb', '0002_candidato_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='partido',
            field=models.CharField(choices=[('Ninguno', 'NINGUNO'), ('MAS-ISPSP', 'MOVIMIENTO AL SOCIALISMO'), ('COMUNIDAD_CIUDADANA', 'COMUNIDAD CIUDADANA'), ('CREEMOS', 'CREEMOS'), ('PARTIDO DEMOCRÁTICO CRISTIANO', 'PARTIDO DEMOCRÁTICO CRISTIANO'), ('LIBERTAR Y DEMOCRACIA', 'LIBERTAD Y DEMOCRACIA'), ('MOVIMIENTO TERCER SISTEMA', 'MOVIMIENTO TERCER SISTEMA'), ('PARTIDO DE ACCION NACIONAL BOLIVIANO', 'PARTIDO DE ACCION NACIONAL BOLIVIANO')], default=1, max_length=40, verbose_name='Partido Político'),
        ),
    ]
