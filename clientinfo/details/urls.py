from django.urls import path
from details.views import register,show_firstname,s_f


urlpatterns = [
    path('register/',register),
    path('show/', show_firstname),
    path('s/', s_f),

]
