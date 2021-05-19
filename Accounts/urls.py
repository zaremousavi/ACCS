from django.urls import path
from .views import ListGroupAcc, CreateGroupAcc, ListKolAcc, CreateKolAcc, CreateMoinAcc, ListMoinAcc, UpdateGroupAcc
from .views import DeleteGroupAcc,UpdateKolAcc, DeleteKolAcc, UpdateMoinAcc, DeleteMoinAcc, ListGroupTaf,   CreateGroupTaf, UpdateGroupTaf, DeleteGroupTaf
from .views import ListTafsili, CreateTafsili, UpdateTafsili, DeleteTafsili
from . import views
app_name = 'Accounts'
urlpatterns = [
    path('ListGroupAcc/',ListGroupAcc.as_view(),name='ListGroupAcc'),
    path('CreateGroupAcc/', CreateGroupAcc.as_view(), name='CreateGroupAcc'),
    path('UpdateGroupAcc/<int:pk>', UpdateGroupAcc.as_view(), name='UpdateGroupAcc'),
    path('DeleteGroupAcc/<int:pk>', DeleteGroupAcc.as_view(), name='DeleteGroupAcc'),

    path('ListKolAcc/', ListKolAcc.as_view(), name='ListKolAcc'),
    path('CreateKolAcc/', CreateKolAcc.as_view(), name='CreateKolAcc'),
    path('UpdateKolAcc/<int:pk>', UpdateKolAcc.as_view(), name='UpdateKolAcc'),
    path('DeleteKolAcc/<int:pk>', DeleteKolAcc.as_view(), name='DeleteKolAcc'),

    path('ListMoinAcc/', ListMoinAcc.as_view(), name='ListMoinAcc'),
    path('CreateMoinAcc/', CreateMoinAcc.as_view(), name='CreateMoinAcc'),
    path('UpdateMoinAcc/<int:pk>', UpdateMoinAcc.as_view(), name='UpdateMoinAcc'),
    path('DeleteMoinAcc/<int:pk>', DeleteMoinAcc.as_view(), name='DeleteMoinAcc'),

    path('ListGroupTaf/', ListGroupTaf.as_view(), name='ListGroupTaf'),
    path('CreateGroupTaf/', CreateGroupTaf.as_view(), name='CreateGroupTaf'),
    path('UpdateGroupTaf/<int:pk>', UpdateGroupTaf.as_view(), name='UpdateGroupTaf'),
    path('DeleteGroupTaf/<int:pk>', DeleteGroupTaf.as_view(), name='DeleteGroupTaf'),

    path('ListTafsili/', ListTafsili.as_view(), name='ListTafsili'),
    path('CreateTafsili/', CreateTafsili.as_view(), name='CreateTafsili'),
    path('UpdateTafsili/<int:pk>', UpdateTafsili.as_view(), name='UpdateTafsili'),
    path('DeleteTafsili/<int:pk>', DeleteTafsili.as_view(), name='DeleteTafsili'),

    path('ListMoinTafsili/',views.ListMoinTafRel , name='ListMoinTafsili'),
    path('CheckGtafs/',views.CheckGtafs.as_view() , name='CheckGtafs'),

]