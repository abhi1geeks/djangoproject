from django.urls import path,include
from . import views
from .newapi_view import *

urlpatterns = [
    # ------ simple using newapi_view.py------#
    path('newapi/profile_all/', ProfileListApi.as_view(),name='profiles'),
    path('newapi/profile_detail/<int:pk>', ProfileDetailsApi.as_view(),name='detail_api'),
    path('newapi/profile_create', ProfileCreateApi.as_view(),name='create_api'),
    path('newapi/profile_update/<int:pk>', ProfileUpdateApi.as_view(),name='update_api'),
    path('newapi/profile_delete/<int:pk>', ProfileDeleteApi.as_view(),name='delete_api'),

    # # ------ simple using view.py------#
    # path('all/', views.profileList,name='profiles'),
    # path('detail/<str:pk>', views.profileDetails,name='detail'),
    # path('create', views.profileCreate,name='create'),
    # path('update/<str:pk>', views.profileUpdate,name='update'),
    # path('delete/<str:pk>', views.profileDelete,name='delete'),
    #--------------------------------------#
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]