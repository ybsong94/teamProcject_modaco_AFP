from django.urls import path

from .views import photo_views

app_name = 'photo'

urlpatterns = [
    # 클래스형 뷰는 뒤에 as_view()가 붙는데 함수형은 안붙는다
    # Photo_views.py
    path('', photo_views.index, name='photo_index'),
    path('create/', photo_views.photo_create, name='photo_create'),

]