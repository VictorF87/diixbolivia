from django.db import models

PARTIDO_POLITICO = [
    ('NINGUNO', 'NINGUNO'),
    ('MOVIMIENTO AL SOCIALISMO', 'MOVIMIENTO AL SOCIALISMO'),
    ('COMUNIDAD CIUDADANA', 'COMUNIDAD CIUDADANA'),
    ('CREEMOS', 'CREEMOS'),
    ('PARTIDO DEMOCRÁTICO CRISTIANO', 'PARTIDO DEMOCRÁTICO CRISTIANO'),
    ('LIBERTAR Y DEMOCRACIA', 'LIBERTAD Y DEMOCRACIA'),
    ('MOVIMIENTO TERCER SISTEMA', 'MOVIMIENTO TERCER SISTEMA'),
    ('PARTIDO DE ACCION NACIONAL BOLIVIANO',
     'PARTIDO DE ACCION NACIONAL BOLIVIANO'),
]


class candidato(models.Model):
    id_cadidato = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(
        max_length=450, blank=False, null=False, verbose_name="Nombre Completo")
    foto = models.ImageField(
        upload_to='fotos/candidatos', verbose_name="Foto del Candidato")
    partido = models.CharField(
        max_length=40, choices=PARTIDO_POLITICO, verbose_name="Partido Político", default=1)
    color = models.CharField(
        max_length=20, verbose_name="Color", blank=False, null=False)
    pdf = models.FileField(upload_to='pdf/candidatos',
                           verbose_name="Plan de Gobierno")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        db_table = 'candidato'

    def __str__(self):
        return self.nombre_completo


class votante(models.Model):
    ci = models.CharField(primary_key=True, max_length=7,
                          verbose_name="Carnet de identidad")
    celular = models.CharField(
        max_length=7, null=False, blank=False, verbose_name="Celular")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")
    candidato_favorito = models.ForeignKey(
        candidato, on_delete=models.CASCADE, verbose_name='Candidato Favorito')

    class Meta:
        verbose_name = 'Votante'
        verbose_name_plural = 'Votantes'
        db_table = 'votante'

    def __str__(self):
        return self.ci
