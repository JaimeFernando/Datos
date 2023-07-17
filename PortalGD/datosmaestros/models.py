from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class CatCategoriaCatalogo(models.Model):
    idcategoriacatalogo = models.AutoField(db_column='idCategoriaCatalogo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=False, null=False)
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=False, null=False)
    esactivo = models.BooleanField(db_column='esActivo', default=True)  # Field name made lowercase.
    orden = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_created=True)
    created_by = models.IntegerField(db_column='created_by')
    updated_at = models.DateTimeField(auto_now=True, auto_created=False)
    updated_by = models.IntegerField(db_column='updated_by')
    deleted_at = models.DateTimeField(auto_now=True, auto_created=False)
    deleted_by = models.IntegerField(db_column='deleted_by')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = False
        db_table = 'cat].[catCategoriaCatalogo'

        verbose_name = 'Categoria del Catalogo'
        verbose_name_plural = 'Categorias de los Catalogos'
    
    def __str__(self):
        return self.nombre


class CatDependencia(models.Model):
    iddependencia = models.AutoField(db_column='idDependencia', primary_key=True)  # Field name made lowercase.
    cvedependencia = models.CharField(db_column='cveDependencia', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    siglas = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    esejecutora = models.BooleanField(db_column='esEjecutora')  # Field name made lowercase.
    esdependenciaschema = models.BooleanField(db_column='esDependenciaSchema')  # Field name made lowercase.
    nombreschema = models.CharField(db_column='nombreSchema', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now=False, auto_created=True)
    created_by = models.IntegerField(db_column='created_by')
    updated_at = models.DateTimeField(auto_now=True, auto_created=False)
    updated_by = models.IntegerField(db_column='updated_by')
    deleted_at = models.DateTimeField(auto_now=True, auto_created=False)
    deleted_by = models.IntegerField(db_column='deleted_by')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = False
        db_table = 'cat].[catDependencia'

        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'
    
    def __str__(self):
        return self.nombre


class CatNivelConfidencialidad(models.Model):
    idnivelconfidencialidad = models.AutoField(db_column='idNivelConfidencialidad', primary_key=True)  # Field name made lowercase.
    nivelconfidencialidad = models.CharField(db_column='NivelConfidencialidad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now=False, auto_created=True)
    created_by = models.IntegerField(db_column='created_by')
    updated_at = models.DateTimeField(auto_now=True, auto_created=False)
    updated_by = models.IntegerField(db_column='updated_by')
    deleted_at = models.DateTimeField(auto_now=True, auto_created=False)
    deleted_by = models.IntegerField(db_column='deleted_by')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = False
        db_table = 'cat].[catNivelConfidencialidad'

        verbose_name = 'Nivel de Confidencialidad'
        verbose_name_plural = 'Niveles de Confidencialidad'
    
    def __str__(self):
        return self.nivelconfidencialidad
    

class CatCatalogo(models.Model):
    idcatalogo = models.AutoField(db_column='idCatalogo', primary_key=True)  # Field name made lowercase.
    iddependencia = models.ForeignKey(CatDependencia, db_column='iddependencia', on_delete=models.DO_NOTHING)
    idcategoriacatalogo = models.ForeignKey(CatCategoriaCatalogo, db_column='idcategoriacatalogo', on_delete=models.DO_NOTHING)
    idnivelconfidencialidad = models.ForeignKey(CatNivelConfidencialidad, db_column='idnivelconfidencialidad', on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descripcion = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    areaatribucion = models.CharField(db_column='areaAtribucion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fundamentojuridico = models.CharField(db_column='fundamentoJuridico', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tabledata = models.CharField(db_column='tableData', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    pathinstructivo = models.CharField(db_column='pathInstructivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apidata = models.CharField(db_column='apiData', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pathinstructivoapidata = models.CharField(db_column='pathInstructivoApiData', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(blank=True, null=True)
    nombrecustodio = models.CharField(db_column='nombreCustodio', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    puestocustodio = models.CharField(db_column='puestoCustodio', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombreduenio = models.CharField(db_column='nombreDuenio', max_length=255, db_collation='Albanian_100_BIN')  # Field name made lowercase.
    puestoduenio = models.CharField(db_column='puestoDuenio', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.IntegerField(db_column='created_by', blank=True, null=True),
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    updated_by = models.IntegerField(db_column='updated_by', blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    deleted_by = models.IntegerField(db_column='deleted_by', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = False
        db_table = 'cat].[catCatalogo'

        verbose_name = 'Catalogos'
        verbose_name_plural = 'Catalogos'
    
    def __str__(self):
        return self.nombre
    