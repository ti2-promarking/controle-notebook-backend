# myproject/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import PessoaViewSet, NotebookViewSet, AluguelViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'notebooks', NotebookViewSet)
router.register(r'alugueis', AluguelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
