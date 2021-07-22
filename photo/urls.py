from django.urls import path
from .views import photo_views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'photo'

urlpatterns = [
    # 클래스형 뷰는 뒤에 as_view()가 붙는데 함수형은 안붙는다
    path('', photo_views.index, name='photo_index'),
    path('form/', photo_views.photo_form, name='photo_form'),
    path('create/', photo_views.photo_create, name='photo_create'),
    path('list/', photo_views.photo_list, name='photo_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)