from django.urls import path
from . import views
from Project_management_app.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('upload/', views.upload, name='upload_book'),
    path('update/<int:book_id>',views.update_book),
    path('delete/<int:book_id>',views.delete),

    path('index1',views.index1,name='index1'),
    path('upload1/',views.upload1,name='upload_book1'),
    path('update1/<int:book_id>',views.update_book1),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)