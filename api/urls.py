from rest_framework import routers
from django.urls import include, path 
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#  router.register(r'number', views.NumberViewSet,'Number' )

urlpatterns = [
    path('', include(router.urls)),
    path('number/', views.NumberList.as_view()),
    path('number/<int:pk>/', views.NumberDetail.as_view()),

]