from django.urls import path
from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

app_name = 'pizzas'

urlpatterns = [
    path('',views.index,name='index'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    path('new_comment/',views.new_comment, name='new_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)