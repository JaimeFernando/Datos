from django.db import models
from simple_history.models import HistoricalRecords
from django.conf import settings


class ControlDateTable(models.Model):
    is_active = models.BooleanField(db_column='is_active', default=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    created_by = models.IntegerField(db_column='created_by')
    updated_at = models.DateTimeField(db_column='updated_at',auto_now=True)
    updated_by = models.IntegerField(db_column='updated_by', null=True)
    deleted_at = models.DateTimeField(db_column='deleted_at', null=True)
    deleted_by = models.IntegerField(db_column='deleted_by',null=True)
    
    class Meta:
        abstract = True
    

# Create your models here.
class CatCategoriaCatalogo(ControlDateTable):
    idcategoriacatalogo = models.AutoField(db_column='idCategoriaCatalogo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    orden = models.IntegerField(blank=True, null=True)

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = True if settings.BRANCH == "isaias" else False
        db_table = 'catCategoriaCatalogo'

        verbose_name = 'Categoria del Catalogo'
        verbose_name_plural = 'Categorias de los Catalogos'
    
    def __str__(self):
        return self.nombre


class CatDependencia(ControlDateTable):
    iddependencia = models.AutoField(db_column='idDependencia', primary_key=True)  # Field name made lowercase.
    cvedependencia = models.CharField(db_column='cveDependencia', max_length=255)  # Field name made lowercase.
    nombre = models.CharField(max_length=255)
    siglas = models.CharField(unique=True, max_length=255)
    esejecutora = models.BooleanField(db_column='esEjecutora')  # Field name made lowercase.
    esdependenciaschema = models.BooleanField(db_column='esDependenciaSchema')  # Field name made lowercase.
    nombreschema = models.CharField(db_column='nombreSchema', max_length=255, blank=True, null=True)  # Field name made lowercase.
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = True if settings.BRANCH == "isaias" else False
        db_table = 'catDependencia'

        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'
    
    def __str__(self):
        return self.nombre


class CatNivelConfidencialidad(ControlDateTable):
    idnivelconfidencialidad = models.AutoField(db_column='idNivelConfidencialidad', primary_key=True)  # Field name made lowercase.
    nivelconfidencialidad = models.CharField(db_column='NivelConfidencialidad', max_length=255,blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = True if settings.BRANCH == "isaias" else False
        db_table = 'catNivelConfidencialidad'

        verbose_name = 'Nivel de Confidencialidad'
        verbose_name_plural = 'Niveles de Confidencialidad'
    
    def __str__(self):
        return self.nivelconfidencialidad
    

class CatCatalogo(ControlDateTable):
    idcatalogo = models.IntegerField(db_column='idCatalogo')
    iddependencia = models.ForeignKey(CatDependencia, db_column='iddependencia', on_delete=models.DO_NOTHING)
    idcategoriacatalogo = models.ForeignKey(CatCategoriaCatalogo, db_column='idcategoriacatalogo', on_delete=models.DO_NOTHING)
    idnivelconfidencialidad = models.ForeignKey(CatNivelConfidencialidad, db_column='idnivelconfidencialidad', on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=500)
    areaatribucion = models.CharField(db_column='areaAtribucion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fundamentojuridico = models.CharField(db_column='fundamentoJuridico', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tabledata = models.CharField(db_column='tableData', max_length=255,   )  # Field name made lowercase.
    pathinstructivo = models.CharField(db_column='pathInstructivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apidata = models.CharField(db_column='apiData', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pathinstructivoapidata = models.CharField(db_column='pathInstructivoApiData', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(blank=True, null=True)
    nombrecustodio = models.CharField(db_column='nombreCustodio', max_length=255,   )  # Field name made lowercase.
    puestocustodio = models.CharField(db_column='puestoCustodio', max_length=255,   )  # Field name made lowercase.
    nombreduenio = models.CharField(db_column='nombreDuenio', max_length=255)  # Field name made lowercase.
    puestoduenio = models.CharField(db_column='puestoDuenio', max_length=255,   )  # Field name made lowercase.

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        managed = True if settings.BRANCH == "isaias" else False
        db_table = 'catCatalogo'

        verbose_name = 'Catalogos'
        verbose_name_plural = 'Catalogos'
    
    def __str__(self):
        return self.nombre
    
    
# catalogos: 10:mortal_kombat,12:yugio
# users : 12,14,132,23,4,5

# en UsuarioApiPermiso vas a tener 2 objetos que van a machear con catCatalogo
# 1 catalogo puede tener muchos usuarios
# catalogo 10-> 12,14,5
# UsuarioCatalogo : users 12:useriocatqalogo:1,users 12:useriocatqalogo:1
# catalogo 12-> 132,23,4,users 12:useriocatqalogo:1

class PermisosUsuario(ControlDateTable):
    permiso_lectura = models.BooleanField(default=True)
    permiso_escritura = models.BooleanField(default=True)
    permiso_eliminacion = models.BooleanField(default=True)
    permiso_actualizacion = models.BooleanField(default=True)
    user =  models.ForeignKey("user.User",on_delete=models.CASCADE)
    catalogo = models.ForeignKey(CatCatalogo,on_delete=models.CASCADE) 