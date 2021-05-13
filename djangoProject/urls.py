from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Company.urls'),name= 'home'),
    path('authent/', include('authent.urls'), name='authent'),
    path('Accounts/', include('Accounts.urls'), name='Accounts'),

]

