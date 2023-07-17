from rest_framework.routers import DefaultRouter
from datosmaestros.api.views.general_views import *
from datosmaestros.api.views.catalogo_viewsets import CatCatalogoViewSet

router = DefaultRouter()

router.register(r'catalogo', CatCatalogoViewSet, basename='Catalogo')#API Master
router.register(r'categoria-catalogo', CatCategoriaCatalogoViewSet, basename='Categoria Catalogo')
router.register(r'dependencia', CatDependenciaViewSet, basename='Dependencia')
router.register(r'nivel-confidencialidad', CatNivelConfidencialidadViewSet, basename='Nivel de Confidencialidad')
router.register(r'catcatalogo', CatCatalogoViewSet, basename= 'catalogo')

urlpatterns = router.urls