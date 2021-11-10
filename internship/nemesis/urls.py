from django.urls import path
from nemesis.views import *
urlpatterns = [
    path('',login,name="login"),
    path('signup/',signup,name="signup"),
    path('register/',register,name="register"),
    path('show_details/',showDetails,name="show_details"),
    path('info/',showInfo,name="info"),
    path('update/<user_id>/',update,name="update"),
    path('delete/<user_id>/',delete,name="delete"),
    path('logout/',logout,name="logout"),
    path('home/',home,name="home"),
    path('contact/',contact,name="contact"),
    path('dashboard/',dashboard,name="dashboard"),
    path('mobiles/',mobiles_info,name="mobiles_info"),
    path('review/<int:m_id>/',review,name='review'),
]
