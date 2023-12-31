# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40, db_collation='Latin1_General_CI_AS')
    created = models.DateTimeField()
    user = models.OneToOneField('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Catagenda(models.Model):
    idagenda = models.IntegerField(db_column='idAgenda', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    idtipoagenda = models.IntegerField(db_column='idTipoAgenda')  # Field name made lowercase.
    nombrecorto = models.CharField(db_column='nombreCorto', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodohasta = models.IntegerField(db_column='periodoHasta', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catAgenda'

    class Meta:
        managed = False
        db_table = 'cat].[catAgenda'

        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
    
    def __str__(self):
        return self.nombrecorto


class Catautonomia(models.Model):
    idautonomia = models.IntegerField(db_column='idAutonomia', primary_key=True)  # Field name made lowercase.
    descripcionautonomia = models.CharField(db_column='descripcionAutonomia', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idanexotransversal = models.IntegerField(db_column='idAnexoTransversal')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catAutonomia'
        unique_together = (('idautonomia', 'idanexotransversal'),)


class Catcalificacioncualitativa(models.Model):
    idcalificacion = models.IntegerField(db_column='idCalificacion', primary_key=True)  # Field name made lowercase.
    calificacion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catCalificacionCualitativa'


class Catcapital(models.Model):
    idcapital = models.IntegerField(db_column='idCapital', primary_key=True)  # Field name made lowercase.
    capital = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catCapital'

    class Meta:
        managed = False
        db_table = 'cat].[catCapital'

        verbose_name = 'Capital'
        verbose_name_plural = 'Capitales'
    
    def __str__(self):
        return self.capital


class Catcapitulo(models.Model):
    idcapitulo = models.IntegerField(db_column='idCapitulo', primary_key=True)  # Field name made lowercase.
    capitulo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    descripcioncapitulo = models.CharField(db_column='descripcionCapitulo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catCapitulo'


class Catcatalogo(models.Model):
    idcatalogo = models.AutoField(db_column='idCatalogo', primary_key=True)  # Field name made lowercase.
    iddependencia = models.IntegerField(db_column='idDependencia')  # Field name made lowercase.
    idcategoriacatalogo = models.IntegerField(db_column='idCategoriaCatalogo')  # Field name made lowercase.
    idnivelconfidencialidad = models.IntegerField(db_column='idNivelConfidencialidad')  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    descripcion = models.CharField(max_length=500, db_collation='Latin1_General_CI_AS')
    areaatribucion = models.CharField(db_column='areaAtribucion', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fundamentojuridico = models.CharField(db_column='fundamentoJuridico', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tabledata = models.CharField(db_column='tableData', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    pathinstructivo = models.CharField(db_column='pathInstructivo', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apidata = models.CharField(db_column='apiData', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pathinstructivoapidata = models.CharField(db_column='pathInstructivoApiData', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(blank=True, null=True)
    nombrecustodio = models.CharField(db_column='nombreCustodio', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    puestocustodio = models.CharField(db_column='puestoCustodio', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombreduenio = models.CharField(db_column='nombreDuenio', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    puestoduenio = models.CharField(db_column='puestoDuenio', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catCatalogo'


class Catcategoria(models.Model):
    idcategoria = models.IntegerField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    color = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    idgrupocategoria = models.IntegerField(db_column='idGrupoCategoria')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catCategoria'


class Catcategoriacatalogo(models.Model):
    idcategoriacatalogo = models.IntegerField(db_column='idCategoriaCatalogo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catCategoriaCatalogo'


class Catcentrotrabajo(models.Model):
    idcct = models.IntegerField(db_column='idCCT', primary_key=True)  # Field name made lowercase.
    clavecct = models.CharField(db_column='claveCCT', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombrecct = models.CharField(db_column='nombreCCT', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    modalidad = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sostenimiento = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estatus = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    domicilio = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    region = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    idmunicipio = models.IntegerField(db_column='idMunicipio')  # Field name made lowercase.
    cp = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    poblacion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    marginacion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    turno = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    provisional = models.BooleanField()
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catCentroTrabajo'


class Catcodigosepomex(models.Model):
    dcodigo = models.CharField(db_column='dCodigo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dasenta = models.CharField(db_column='dAsenta', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dtipoasenta = models.CharField(db_column='dTipoAsenta', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dmnpio = models.CharField(db_column='dMnpio', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    destado = models.CharField(db_column='dEstado', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dciudad = models.CharField(db_column='dCiudad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dcp = models.CharField(db_column='dCP', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cestado = models.CharField(db_column='cEstado', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coficina = models.CharField(db_column='cOficina', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccp = models.CharField(db_column='cCP', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ctipoasenta = models.CharField(db_column='cTipoAsenta', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cmnpio = models.CharField(db_column='cMnpio', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idasentacpcons = models.CharField(db_column='idAsentaCPcons', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dzona = models.CharField(db_column='dZona', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccveciudad = models.CharField(db_column='cCveCiudad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idcodigopostal = models.BigAutoField(db_column='idCodigoPostal', primary_key=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catCodigoSepomex'


class Catcomponente(models.Model):
    idcomponente = models.IntegerField(db_column='idComponente', primary_key=True)  # Field name made lowercase.
    idprogramapresupuestario = models.IntegerField(db_column='idProgramaPresupuestario')  # Field name made lowercase.
    clavecomponente = models.CharField(db_column='claveComponente', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    componente = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ejercicio = models.IntegerField()
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catComponente'


class Catcontratista(models.Model):
    idcontratista = models.IntegerField(db_column='idContratista', primary_key=True)  # Field name made lowercase.
    contratista = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catContratista'


class Catcontribucion(models.Model):
    idcontribucion = models.IntegerField(db_column='IdContribucion', primary_key=True)  # Field name made lowercase.
    idanexotransversal = models.IntegerField(db_column='idAnexoTransversal')  # Field name made lowercase.
    descripcioncontibuci¾n = models.CharField(db_column='descripcionContibuci¾n', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catContribucion'
        unique_together = (('idcontribucion', 'idanexotransversal'),)


class Catdependencia(models.Model):
    iddependencia = models.IntegerField(db_column='idDependencia', primary_key=True)  # Field name made lowercase.
    cvedependencia = models.CharField(db_column='cveDependencia', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    siglas = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    esejecutora = models.BooleanField(db_column='esEjecutora')  # Field name made lowercase.
    esdependenciaschema = models.BooleanField(db_column='esDependenciaSchema')  # Field name made lowercase.
    nombreschema = models.CharField(db_column='nombreSchema', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catDependencia'


class Catderechosocial(models.Model):
    idderechosocial = models.IntegerField(db_column='idDerechoSocial', primary_key=True)  # Field name made lowercase.
    derechosocial = models.CharField(db_column='derechoSocial', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catDerechoSocial'


class Catdesca(models.Model):
    iddesca = models.IntegerField(db_column='idDesca', primary_key=True)  # Field name made lowercase.
    descripciondesca = models.CharField(db_column='descripcionDesca', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catDesca'


class Catdimensionmedida(models.Model):
    iddimension = models.IntegerField(db_column='idDimension', primary_key=True)  # Field name made lowercase.
    dimension = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catDimensionMedida'


class Catdistritoelectoralfederal(models.Model):
    iddistritofederal = models.IntegerField(db_column='idDistritoFederal', primary_key=True)  # Field name made lowercase.
    distritoelectoralfederal = models.CharField(db_column='distritoElectoralFederal', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idmunicipiocabeceradistrito = models.IntegerField(db_column='idMunicipioCabeceraDistrito')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catDistritoElectoralFederal'


class Catdistritoelectorallocal(models.Model):
    iddistritolocal = models.IntegerField(db_column='idDistritoLocal', primary_key=True)  # Field name made lowercase.
    distritoelectorallocal = models.CharField(db_column='distritoElectoralLocal', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catDistritoElectoralLocal'


class Cateje(models.Model):
    ideje = models.IntegerField(db_column='idEje', primary_key=True)  # Field name made lowercase.
    eje = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    periodo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    color = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEje'


class Catejeestrategico(models.Model):
    idejeestrategico = models.IntegerField(db_column='idEjeEstrategico', primary_key=True)  # Field name made lowercase.
    ejeestrategico = models.CharField(db_column='ejeEstrategico', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descejeestrategico = models.CharField(db_column='descEjeEstrategico', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEjeEstrategico'


class Catelementoinstrumento(models.Model):
    idelementoinstrumento = models.IntegerField(db_column='idElementoInstrumento', primary_key=True)  # Field name made lowercase.
    idinstrumentoplaneacion = models.IntegerField(db_column='idInstrumentoPlaneacion')  # Field name made lowercase.
    elementoinstrumento = models.CharField(db_column='elementoInstrumento', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numeroelementoinstrumento = models.CharField(db_column='numeroElementoInstrumento', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombrecorto = models.CharField(db_column='nombreCorto', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periodoinicio = models.IntegerField(db_column='periodoInicio')  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at_field = models.DateTimeField(db_column='created_at ')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    idelementoinstrumentoiplaneg = models.CharField(db_column='idElementoInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catElementoInstrumento'


class Catenfoque(models.Model):
    idenfoque = models.IntegerField(db_column='idEnfoque', primary_key=True)  # Field name made lowercase.
    enfoque = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    idtipoenfoque = models.IntegerField(db_column='idTipoEnfoque')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEnfoque'


class Catestado(models.Model):
    idestado = models.IntegerField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    poligono = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    poligonogeo = models.TextField(db_column='poligonoGeo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstado'


class Catestadocivil(models.Model):
    idestadocivil = models.IntegerField(db_column='idEstadoCivil', primary_key=True)  # Field name made lowercase.
    descripcionestadocivil = models.CharField(db_column='descripcionEstadoCivil', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstadoCivil'


class Catestatusavance(models.Model):
    idestatusavance = models.IntegerField(db_column='idEstatusAvance', primary_key=True)  # Field name made lowercase.
    estatusavance = models.CharField(db_column='estatusAvance', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    idestatusejecutivo = models.IntegerField(db_column='idEstatusEjecutivo')  # Field name made lowercase.
    orden = models.IntegerField()
    tipo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstatusAvance'


class Catestatusejecutivo(models.Model):
    idestatusejecutivo = models.IntegerField(db_column='idEstatusEjecutivo', primary_key=True)  # Field name made lowercase.
    estatusejecutivo = models.CharField(db_column='estatusEjecutivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstatusEjecutivo'


class Catestatusobraaccion(models.Model):
    idestatusobraaccion = models.IntegerField(db_column='idEstatusObraAccion', primary_key=True)  # Field name made lowercase.
    estatusobraaccion = models.CharField(db_column='estatusObraAccion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    representacion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    descripciondgpi = models.CharField(db_column='descripcionDGPI', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstatusObraAccion'


class Catestatusobracontratista(models.Model):
    idestatusobracontratista = models.IntegerField(db_column='idEstatusObraContratista', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstatusObraContratista'


class Catestatustickets(models.Model):
    idestatusticket = models.IntegerField(db_column='idEstatusTicket', primary_key=True)  # Field name made lowercase.
    estatusticket = models.CharField(db_column='estatusTicket', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstatusTickets'


class Catestrategiainstrumento(models.Model):
    idestrategiainstrumento = models.IntegerField(db_column='idEstrategiaInstrumento', primary_key=True)  # Field name made lowercase.
    idobjetivoinstrumento = models.IntegerField(db_column='idObjetivoInstrumento')  # Field name made lowercase.
    numeroestrategia = models.CharField(db_column='numeroEstrategia', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estrategia = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    periodoinicio = models.IntegerField(db_column='periodoInicio')  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    idestrategiainstrumentoiplaneg = models.CharField(db_column='idEstrategiaInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catEstrategiaInstrumento'


class Catestrategiapg(models.Model):
    idestrategiapg = models.AutoField(db_column='idEstrategiaPG', primary_key=True)  # Field name made lowercase.
    idobjetivopg = models.IntegerField(db_column='idObjetivoPG')  # Field name made lowercase.
    claveestrategia = models.CharField(db_column='claveEstrategia', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombreestrategia = models.CharField(db_column='nombreEstrategia', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periodoinicio = models.IntegerField(db_column='periodoInicio')  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEstrategiaPG'
        unique_together = (('idestrategiapg', 'idobjetivopg'),)


class Catetapadesarrollo(models.Model):
    idetapadesarrollo = models.IntegerField(db_column='idEtapaDesarrollo', primary_key=True)  # Field name made lowercase.
    idanexotransversal = models.IntegerField(db_column='idAnexoTransversal')  # Field name made lowercase.
    descripcionetapadesarrollo = models.CharField(db_column='descripcionEtapaDesarrollo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEtapaDesarrollo'
        unique_together = (('idetapadesarrollo', 'idanexotransversal'),)


class Cateventobitacora(models.Model):
    ideventobitacora = models.IntegerField(db_column='idEventoBitacora', primary_key=True)  # Field name made lowercase.
    nombreevento = models.CharField(db_column='nombreEvento', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catEventoBitacora'


class Catfondo(models.Model):
    idfondo = models.IntegerField(db_column='idFondo', primary_key=True)  # Field name made lowercase.
    descripcionfondo = models.CharField(db_column='descripcionFondo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catFondo'


class Catgrupocategoria(models.Model):
    idgrupocategoria = models.IntegerField(db_column='idGrupoCategoria', primary_key=True)  # Field name made lowercase.
    grupocategoria = models.CharField(db_column='grupoCategoria', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    color = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catGrupoCategoria'


class Catgrupoderecho(models.Model):
    idgrupoderecho = models.IntegerField(db_column='idGrupoDerecho', primary_key=True)  # Field name made lowercase.
    descripciongrupoderecho = models.CharField(db_column='descripcionGrupoDerecho', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idanexotransversal = models.IntegerField(db_column='idAnexoTransversal')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catGrupoDerecho'
        unique_together = (('idgrupoderecho', 'idanexotransversal'),)


class Catigualdad(models.Model):
    idigualdad = models.IntegerField(db_column='idIgualdad', primary_key=True)  # Field name made lowercase.
    descripcionigualdad = models.CharField(db_column='descripcionIgualdad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idanexotransversal = models.IntegerField(db_column='idAnexoTransversal')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catIgualdad'
        unique_together = (('idigualdad', 'idanexotransversal'),)


class Catindicadoriplaneg(models.Model):
    idindicador = models.IntegerField(db_column='idIndicador', primary_key=True)  # Field name made lowercase.
    idinstrumentoplaneacioniplaneg = models.CharField(db_column='idInstrumentoPlaneacionIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idelementoinstrumentoiplaneg = models.CharField(db_column='idElementoInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idlineaestrategicainstrumentoiplaneg = models.CharField(db_column='idLineaEstrategicaInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idobjetivoinstrumentoiplaneg = models.CharField(db_column='idObjetivoInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idindicadoriplaneg = models.CharField(db_column='idIndicadorIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descripcionindicador = models.CharField(db_column='descripcionIndicador', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catIndicadorIPLANEG'


class Catinstrumentoplaneacion(models.Model):
    idinstrumentoplaneacion = models.IntegerField(db_column='idInstrumentoPlaneacion', primary_key=True)  # Field name made lowercase.
    instrumentoplaneacion = models.CharField(db_column='instrumentoPlaneacion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numeroinstrumentoplaneacion = models.CharField(db_column='numeroInstrumentoPlaneacion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esprogramadegobierno = models.BooleanField(db_column='esProgramaDeGobierno')  # Field name made lowercase.
    tieneestructura = models.BooleanField(db_column='tieneEstructura')  # Field name made lowercase.
    periodoinicio = models.IntegerField(db_column='periodoInicio')  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin')  # Field name made lowercase.
    esanexo = models.BooleanField(db_column='esAnexo')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    idinstrumentoplaneacioniplaneg = models.CharField(db_column='idInstrumentoPlaneacionIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catInstrumentoPlaneacion'


class Catlineaaccioninstrumento(models.Model):
    idlineaaccioninstrumento = models.IntegerField(db_column='idLineaAccionInstrumento', primary_key=True)  # Field name made lowercase.
    idestrategiainstrumento = models.IntegerField(db_column='idEstrategiaInstrumento')  # Field name made lowercase.
    numerolineaaccion = models.CharField(db_column='numeroLineaAccion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lineaaccion = models.CharField(db_column='lineaAccion', max_length=700, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periodoinicio = models.IntegerField(db_column='periodoInicio')  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin')  # Field name made lowercase.
    idelementoinstrumento = models.IntegerField(db_column='idElementoInstrumento')  # Field name made lowercase.
    idobjetivoinstrumento = models.IntegerField(db_column='idObjetivoInstrumento')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    idlineaaccioninstrumentoiplaneg = models.CharField(db_column='idLineaAccionInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catLineaAccionInstrumento'


class Catlineaestrategicainstrumento(models.Model):
    idlineaestrategicainstrumento = models.IntegerField(db_column='idLineaEstrategicaInstrumento', primary_key=True)  # Field name made lowercase.
    idelementoinstrumento = models.IntegerField(db_column='idElementoInstrumento')  # Field name made lowercase.
    numerolineaestrategica = models.CharField(db_column='numeroLineaEstrategica', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lineaestrategica = models.TextField(db_column='lineaEstrategica', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periodoinicio = models.IntegerField(db_column='periodoInicio')  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    idlineaestrategicainstrumentoiplaneg = models.CharField(db_column='idLineaEstrategicaInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catLineaEstrategicaInstrumento'


class Catlocalidad(models.Model):
    idlocalidad = models.IntegerField(db_column='idLocalidad')  # Field name made lowercase.
    clavelocalidad = models.CharField(db_column='claveLocalidad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    idestado = models.IntegerField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    idmunicipio = models.IntegerField(db_column='idMunicipio')  # Field name made lowercase.
    tipolocalidad = models.CharField(db_column='tipoLocalidad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    altitud = models.FloatField(blank=True, null=True)
    poblaciontotal = models.IntegerField(db_column='poblacionTotal', blank=True, null=True)  # Field name made lowercase.
    poblacionmasculina = models.IntegerField(db_column='poblacionMasculina', blank=True, null=True)  # Field name made lowercase.
    poblacionfemenina = models.IntegerField(db_column='poblacionFemenina', blank=True, null=True)  # Field name made lowercase.
    totalviviendashabitadas = models.IntegerField(db_column='totalViviendasHabitadas', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catLocalidad '
        unique_together = (('idestado', 'idmunicipio', 'idlocalidad'),)


class Catmes(models.Model):
    idmes = models.IntegerField(db_column='idMes', primary_key=True)  # Field name made lowercase.
    mes = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nombrecortomes = models.CharField(db_column='nombreCortoMes', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catMes'


class Catmetaiplaneg(models.Model):
    idmeta = models.IntegerField(db_column='idMeta', primary_key=True)  # Field name made lowercase.
    idinstrumentoplaneacioniplaneg = models.CharField(db_column='idInstrumentoPlaneacionIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idelementoinstrumentoiplaneg = models.CharField(db_column='idElementoInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idlineaestrategicainstrumentoiplaneg = models.CharField(db_column='idLineaEstrategicaInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idobjetivoinstrumentoiplaneg = models.CharField(db_column='idObjetivoInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idindicadoriplaneg = models.CharField(db_column='idIndicadorIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    idmetaiplaneg = models.CharField(db_column='idMetaIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descripcionmeta = models.CharField(db_column='descripcionMeta', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catMetaIPLANEG'


class Catmodalidadcontratacion(models.Model):
    idmodalidadcontratacion = models.IntegerField(db_column='idModalidadContratacion', primary_key=True)  # Field name made lowercase.
    modalidad = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catModalidadContratacion'


class Catmunicipio(models.Model):
    idmunicipio = models.IntegerField(db_column='idMunicipio')  # Field name made lowercase.
    idestado = models.IntegerField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    clavemunicipio = models.CharField(db_column='claveMunicipio', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombremunicipio = models.CharField(db_column='nombreMunicipio', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    poligono = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    poligonogeo = models.TextField(db_column='poligonoGeo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catMunicipio'
        unique_together = (('idestado', 'idmunicipio'),)


class Catnivelconfidencialidad(models.Model):
    idnivelconfidencialidad = models.IntegerField(db_column='idNivelConfidencialidad', primary_key=True)  # Field name made lowercase.
    nivelconfidencialidad = models.CharField(db_column='NivelConfidencialidad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catNivelConfidencialidad'


class Catods(models.Model):
    idods = models.IntegerField(db_column='idODS', primary_key=True)  # Field name made lowercase.
    ods = models.CharField(db_column='ODS', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    objetivo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    numeroods = models.IntegerField(db_column='numeroODS')  # Field name made lowercase.
    rutaimagen = models.CharField(db_column='rutaImagen', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catODS'


class Catobjetivo(models.Model):
    idobjetivo = models.IntegerField(db_column='idObjetivo', primary_key=True)  # Field name made lowercase.
    idanexotransversal = models.IntegerField(db_column='idAnexoTransversal')  # Field name made lowercase.
    descripcionobjetivo = models.CharField(db_column='descripcionObjetivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catObjetivo'
        unique_together = (('idobjetivo', 'idanexotransversal'),)


class Catobjetivocontigosi(models.Model):
    idobjetivocontigosi = models.IntegerField(db_column='idObjetivoContigoSi', primary_key=True)  # Field name made lowercase.
    objetivocontigosi = models.TextField(db_column='objetivoContigoSi', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    componente = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catObjetivoContigoSi'


class Catobjetivoinstrumento(models.Model):
    idobjetivoinstrumento = models.IntegerField(db_column='idObjetivoInstrumento', primary_key=True)  # Field name made lowercase.
    idlineaestrategicainstrumento = models.IntegerField(db_column='idLineaEstrategicaInstrumento')  # Field name made lowercase.
    idelementoinstrumento = models.IntegerField(db_column='idElementoInstrumento')  # Field name made lowercase.
    idestrategiapg = models.IntegerField(db_column='idEstrategiaPG')  # Field name made lowercase.
    numeroobjetivo = models.CharField(db_column='numeroObjetivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombreobjetivo = models.CharField(db_column='nombreObjetivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periodoinicio = models.IntegerField(db_column='periodoInicio')  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    idobjetivoinstrumentoiplaneg = models.CharField(db_column='idObjetivoInstrumentoIPLANEG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catObjetivoInstrumento'


class Catobjetivopg(models.Model):
    idobjetivopg = models.AutoField(db_column='idObjetivoPG', primary_key=True)  # Field name made lowercase.
    claveobjetivo = models.CharField(db_column='claveObjetivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombreobjetivo = models.CharField(db_column='nombreObjetivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ideje = models.IntegerField(db_column='idEje')  # Field name made lowercase.
    periodoinicio = models.IntegerField(db_column='periodoInicio', blank=True, null=True)  # Field name made lowercase.
    periodofin = models.IntegerField(db_column='periodoFin', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catObjetivoPG'


class Catorigendato(models.Model):
    idorigendato = models.IntegerField(db_column='idOrigenDato', primary_key=True)  # Field name made lowercase.
    origendato = models.CharField(db_column='OrigenDato', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catOrigenDato'


class Catpais(models.Model):
    idpais = models.IntegerField(db_column='idPais', primary_key=True)  # Field name made lowercase.
    nombrecortoingles = models.CharField(db_column='nombreCortoIngles', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombrecortofrances = models.CharField(db_column='nombreCortoFrances', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codigoalpha2 = models.CharField(db_column='codigoAlpha2', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    codigoalpha3 = models.CharField(db_column='codigoAlpha3', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    numerico = models.IntegerField()
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catPais'


class Catpartida(models.Model):
    idpatida = models.IntegerField(db_column='idPatida', primary_key=True)  # Field name made lowercase.
    descripcionpartida = models.CharField(db_column='descripcionPartida', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idcapitulo = models.IntegerField(db_column='idCapitulo')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catPartida'


class Catprogramapresupuestario(models.Model):
    idprogramapresupuestario = models.IntegerField(db_column='idProgramaPresupuestario', primary_key=True)  # Field name made lowercase.
    claveprogramapresupuestario = models.CharField(db_column='claveProgramaPresupuestario', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nombreprograma = models.CharField(db_column='nombrePrograma', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ejercicio = models.IntegerField()
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catProgramaPresupuestario'


class Catramo(models.Model):
    idramo = models.IntegerField(db_column='idRamo', primary_key=True)  # Field name made lowercase.
    ramo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catRamo'


class Catregion(models.Model):
    idregion = models.AutoField(db_column='idRegion', primary_key=True)  # Field name made lowercase.
    numeroregion = models.CharField(db_column='numeroRegion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcionregion = models.CharField(db_column='descripcionRegion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catRegion'


class Catsedtipoproyecto(models.Model):
    idtipoproyecto = models.IntegerField(db_column='idTipoProyecto', primary_key=True)  # Field name made lowercase.
    clavetipoproyecto = models.IntegerField(db_column='claveTipoProyecto', blank=True, null=True)  # Field name made lowercase.
    tipoproyecto = models.CharField(db_column='tipoProyecto', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catSEDTipoProyecto'


class Catsexenio(models.Model):
    idsexenio = models.IntegerField(db_column='idSexenio', primary_key=True)  # Field name made lowercase.
    periodo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catSexenio'


class Catsituacion(models.Model):
    idsituacion = models.IntegerField(db_column='idSituacion', primary_key=True)  # Field name made lowercase.
    situacion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    descsituacion = models.CharField(db_column='descSituacion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catSituacion'


class Catsubcategoria(models.Model):
    idcategoria = models.IntegerField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    idsubcategoria = models.IntegerField(db_column='idSubCategoria')  # Field name made lowercase.
    subcategoria = models.CharField(db_column='subCategoria', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catSubCategoria'
        unique_together = (('idcategoria', 'idsubcategoria'),)


class Catsubejeestrategico(models.Model):
    idsubejeestrategico = models.IntegerField(db_column='idSubEjeEstrategico', primary_key=True)  # Field name made lowercase.
    idejeestrategico = models.IntegerField(db_column='idEjeEstrategico')  # Field name made lowercase.
    subejeestrategico = models.CharField(db_column='subEjeEstrategico', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catSubEjeEstrategico'
        unique_together = (('idsubejeestrategico', 'idejeestrategico'),)


class Catsubtemaderecho(models.Model):
    idsubtemaderecho = models.IntegerField(db_column='idSubTemaDerecho', primary_key=True)  # Field name made lowercase.
    idanexotransversal = models.IntegerField(db_column='idAnexoTransversal')  # Field name made lowercase.
    descripcionsubtemaderecho = models.CharField(db_column='descripcionSubTemaDerecho', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo_field = models.BooleanField(db_column='esActivo ')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catSubTemaDerecho'
        unique_together = (('idsubtemaderecho', 'idanexotransversal'),)


class Cattematicaatencion(models.Model):
    idtematicaatencion = models.IntegerField(db_column='idTematicaAtencion', primary_key=True)  # Field name made lowercase.
    cvetematicaatencion = models.CharField(db_column='cveTematicaAtencion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tematicaatencion = models.CharField(db_column='tematicaAtencion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTematicaAtencion'


class Cattipo(models.Model):
    idtipo = models.IntegerField(db_column='idTipo', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    obra = models.BooleanField(blank=True, null=True)
    accion = models.BooleanField(blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipo'


class Cattipoaccion(models.Model):
    idtipoaccion = models.IntegerField(db_column='idTipoAccion', primary_key=True)  # Field name made lowercase.
    tipoaccion = models.CharField(db_column='tipoAccion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoAccion'


class Cattipoagenda(models.Model):
    idtipoagenda = models.IntegerField(db_column='idTipoAgenda', primary_key=True)  # Field name made lowercase.
    tipoagenda = models.CharField(db_column='tipoAgenda', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obligatoria = models.BooleanField()
    seleccionmultiple = models.BooleanField(db_column='seleccionMultiple')  # Field name made lowercase.
    periodohasta = models.IntegerField(db_column='periodoHasta', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoAgenda'


class Cattipoasentamiento(models.Model):
    idtipoasentamiento = models.IntegerField(db_column='idTipoAsentamiento', primary_key=True)  # Field name made lowercase.
    tipoasentamiento = models.CharField(db_column='tipoAsentamiento', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoAsentamiento'


class Cattipobeneficiario(models.Model):
    idtipobeneficiario = models.AutoField(db_column='idTipoBeneficiario', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descripcion = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    icono = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    validoanexo = models.BooleanField(db_column='validoAnexo')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoBeneficiario'


class Cattipoconcurrencia(models.Model):
    idtipoconcurrencia = models.IntegerField(db_column='idTipoConcurrencia', primary_key=True)  # Field name made lowercase.
    tipoconcurrencia = models.CharField(db_column='tipoConcurrencia', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoConcurrencia'


class Cattipoenfoque(models.Model):
    idtipoenfoque = models.IntegerField(db_column='idTipoEnfoque', primary_key=True)  # Field name made lowercase.
    tipoenfoque = models.CharField(db_column='tipoEnfoque', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoEnfoque'


class Cattipogasto(models.Model):
    idtipogasto = models.IntegerField(db_column='idTipoGasto', primary_key=True)  # Field name made lowercase.
    descripciontipogasto = models.CharField(db_column='descripcionTipoGasto', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoGasto'


class Cattipogeoreferencia(models.Model):
    idtipogeoreferencia = models.IntegerField(db_column='idTipoGeoreferencia', primary_key=True)  # Field name made lowercase.
    tipogeoreferencia = models.CharField(db_column='tipoGeoreferencia', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoGeoreferencia'


class Cattipoobraaccion(models.Model):
    idtipoobraaccion = models.IntegerField(db_column='idTipoObraAccion', primary_key=True)  # Field name made lowercase.
    tipoobraaccion = models.CharField(db_column='tipoObraAccion', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoObraAccion'


class Cattipoobraacciong1(models.Model):
    idtipoobraacciong1 = models.IntegerField(db_column='idTipoObraAccionG1', primary_key=True)  # Field name made lowercase.
    tipoobraacciong1 = models.CharField(db_column='tipoObraAccionG1', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoObraAccionG1'


class Cattipopadronbeneficiario(models.Model):
    idtipopadron = models.IntegerField(db_column='idTipoPadron', primary_key=True)  # Field name made lowercase.
    tipopadron = models.CharField(db_column='tipoPadron', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by_field = models.IntegerField(db_column='deleted_by ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'catTipoPadronBeneficiario'


class Cattipovialidad(models.Model):
    idtipovialidad = models.IntegerField(db_column='idTipoVialidad', primary_key=True)  # Field name made lowercase.
    tipovialidad = models.CharField(db_column='tipoVialidad', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catTipoVialidad'


class Catunidadmedida(models.Model):
    idunidadmedida = models.IntegerField(db_column='idUnidadMedida', primary_key=True)  # Field name made lowercase.
    iddimension = models.IntegerField(db_column='idDimension')  # Field name made lowercase.
    unidadmedida = models.CharField(db_column='unidadMedida', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clave = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catUnidadMedida'


class Catunidadmeta(models.Model):
    idunidadmeta = models.IntegerField(db_column='idUnidadMeta', primary_key=True)  # Field name made lowercase.
    unidadmeta = models.CharField(db_column='unidadMeta', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idunidadmedida = models.IntegerField(db_column='idUnidadMedida')  # Field name made lowercase.
    educativo = models.BooleanField(blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catUnidadMeta'


class Catzonaimpulso(models.Model):
    ejercicio = models.IntegerField()
    idzonaimpulso = models.IntegerField(db_column='idZonaImpulso', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cvemun = models.IntegerField(db_column='cveMun', blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    poblaciontotal = models.BigIntegerField(db_column='poblacionTotal', blank=True, null=True)  # Field name made lowercase.
    viviendatotal = models.BigIntegerField(db_column='viviendaTotal', blank=True, null=True)  # Field name made lowercase.
    personaencuestada = models.IntegerField(db_column='personaEncuestada', blank=True, null=True)  # Field name made lowercase.
    viviendaencuestada = models.IntegerField(db_column='viviendaEncuestada', blank=True, null=True)  # Field name made lowercase.
    geometry = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    coordenadascentro = models.CharField(db_column='coordenadasCentro', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    etapa = models.IntegerField(blank=True, null=True)
    cveimpulso = models.CharField(db_column='cveImpulso', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    poligono = models.TextField(blank=True, null=True)  # This field type is a guess.
    poligonotemp = models.TextField(db_column='poligonoTemp', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    poligonotemp2 = models.TextField(db_column='poligonoTemp2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_at = models.DateTimeField()
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catZonaImpulso'


class DatosmaestrosHistoricalcatcatalogo(models.Model):
    created_at = models.DateTimeField()
    idcatalogo = models.IntegerField(db_column='idCatalogo')  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    descripcion = models.CharField(max_length=500, db_collation='Latin1_General_CI_AS')
    areaatribucion = models.CharField(db_column='areaAtribucion', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fundamentojuridico = models.CharField(db_column='fundamentoJuridico', max_length=500, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tabledata = models.CharField(db_column='tableData', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    pathinstructivo = models.CharField(db_column='pathInstructivo', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apidata = models.CharField(db_column='apiData', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pathinstructivoapidata = models.CharField(db_column='pathInstructivoApiData', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(blank=True, null=True)
    nombrecustodio = models.CharField(db_column='nombreCustodio', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    puestocustodio = models.CharField(db_column='puestoCustodio', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    nombreduenio = models.CharField(db_column='nombreDuenio', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    puestoduenio = models.CharField(db_column='puestoDuenio', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    history_type = models.CharField(max_length=1, db_collation='Latin1_General_CI_AS')
    history_user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)
    idcategoriacatalogo = models.IntegerField(blank=True, null=True)
    iddependencia = models.IntegerField(blank=True, null=True)
    idnivelconfidencialidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosmaestros_historicalcatcatalogo'


class DatosmaestrosHistoricalcatcategoriacatalogo(models.Model):
    created_at = models.DateTimeField()
    idcategoriacatalogo = models.IntegerField(db_column='idCategoriaCatalogo')  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    descripcion = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    orden = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_at = models.DateTimeField()
    updated_by = models.IntegerField()
    deleted_at = models.DateTimeField()
    deleted_by = models.IntegerField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    history_type = models.CharField(max_length=1, db_collation='Latin1_General_CI_AS')
    history_user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosmaestros_historicalcatcategoriacatalogo'


class DatosmaestrosHistoricalcatdependencia(models.Model):
    created_at = models.DateTimeField()
    iddependencia = models.IntegerField(db_column='idDependencia')  # Field name made lowercase.
    cvedependencia = models.CharField(db_column='cveDependencia', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    siglas = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    esejecutora = models.BooleanField(db_column='esEjecutora')  # Field name made lowercase.
    esdependenciaschema = models.BooleanField(db_column='esDependenciaSchema')  # Field name made lowercase.
    nombreschema = models.CharField(db_column='nombreSchema', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_by = models.IntegerField()
    updated_at = models.DateTimeField()
    updated_by = models.IntegerField()
    deleted_at = models.DateTimeField()
    deleted_by = models.IntegerField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    history_type = models.CharField(max_length=1, db_collation='Latin1_General_CI_AS')
    history_user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosmaestros_historicalcatdependencia'


class DatosmaestrosHistoricalcatnivelconfidencialidad(models.Model):
    created_at = models.DateTimeField()
    idnivelconfidencialidad = models.IntegerField(db_column='idNivelConfidencialidad')  # Field name made lowercase.
    nivelconfidencialidad = models.CharField(db_column='NivelConfidencialidad', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    esactivo = models.BooleanField(db_column='esActivo')  # Field name made lowercase.
    created_by = models.IntegerField()
    updated_at = models.DateTimeField()
    updated_by = models.IntegerField()
    deleted_at = models.DateTimeField()
    deleted_by = models.IntegerField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    history_type = models.CharField(max_length=1, db_collation='Latin1_General_CI_AS')
    history_user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosmaestros_historicalcatnivelconfidencialidad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Latin1_General_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Latin1_General_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Latin1_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')
    model = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Latin1_General_CI_AS')
    session_data = models.TextField(db_collation='Latin1_General_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UserHistoricaluser(models.Model):
    id = models.BigIntegerField()
    password = models.CharField(max_length=128, db_collation='Latin1_General_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    email = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    last_name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    image = models.TextField(db_collation='Latin1_General_CI_AS', blank=True, null=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    history_type = models.CharField(max_length=1, db_collation='Latin1_General_CI_AS')
    history_user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_historicaluser'


class UserUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, db_collation='Latin1_General_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=255, db_collation='Latin1_General_CI_AS')
    email = models.CharField(unique=True, max_length=255, db_collation='Latin1_General_CI_AS')
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    last_name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    image = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_user'


class UserUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('user', 'group'),)


class UserUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_user_permissions'
        unique_together = (('user', 'permission'),)
