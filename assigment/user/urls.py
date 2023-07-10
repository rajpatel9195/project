from django.urls import path
from .views import createUpdate , getDelete
urlpatterns = [
            path('Delete/<int:pk>',getDelete.as_view(),name = "Delete"),
            path('get',getDelete.as_view(),name = "get"),

            path('Update/<int:pk>',createUpdate.as_view(),name = "Update"),
            path('create',createUpdate.as_view(),name = "create")


]
