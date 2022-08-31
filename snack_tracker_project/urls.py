from django.contrib import admin
from django.urls import include, path
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/',SnackDetailView.as_view(), name='snack_detail'),
    # path("admin/", admin.site.urls),
    # path("", include("snacks.urls"))
]