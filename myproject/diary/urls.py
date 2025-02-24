from django.urls import path
from . import views


app_name = "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
    path("page/list/", views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.page_detail, name="page_detail"),
    path("page/<uuid:id>/update/", views.page_update, name="page_update"),
    path("page/<uuid:id>/delete/", views.page_delete, name="page_delete"),
    path("page/<uuid:id>/answer/", views.page_answer, name="page_answer"),
    path("page/<uuid:id>/answer/list/", views.page_answer_list, name="page_answer_list"),
    path("page/<uuid:id>/answer/check/", views.page_answer_check, name="page_answer_check"),
]