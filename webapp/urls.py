from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="HomePage"),
    path('about/', views.about_page, name="AboutPage"),
    path('orphan/', views.orphan_page, name="OrphanPage"),
    path('contact/', views.contact_page, name="ContactPage"),

    path('login/', views.user_login, name="LogPage"),
    path('logout/', views.user_logout, name="Logout"),
    path('adminpanel/', views.adminpanel_page, name="AdminPanel"),

    path('addorphan/', views.add_orphan, name='add-orphan'),
    path('editorphan/<int:pk>', views.edit_orphan, name='edit-orphan'),
    path('deletepizza/<int:pk>', views.delete_orphan, name='delete-orphan'),
    path('vieworphan/<int:pk>', views.view_orphan, name='view-orphan'),

    path('addoguardian/', views.add_guardian, name='add-guardian'),
    path('editguardian/<int:pk>', views.edit_guardian, name='edit-guardian'),
    path('deleteguardian/<int:pk>', views.delete_guardian, name='delete-guardian'),
]


