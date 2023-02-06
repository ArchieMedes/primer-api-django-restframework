from rest_framework import routers
# View Set
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls # this is for the rest_framework creates our URLs
# this (router) generates like 4 URLs: Create, Read, Update, Delete
