from django.urls import path
from . import views, htmx_views 
urlpatterns = [
    path("", views.index, name='index'),
]
htmx_patterns = [
    path("check_product/", htmx_views.check_product, name='check_product'),
    path("save_product/", htmx_views.save_product, name='save_product'),
    path("delete_product/<int:id>/", htmx_views.delete_product, name='delete_product'),
]

urlpatterns += htmx_patterns
