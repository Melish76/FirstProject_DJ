from django.contrib import admin
from django.urls import path
from . import views # import views yazanda sehf verir cwnki django . noqte qoyaraq demek isteyir ki bu klasordaki views
from django.conf import settings
from django.conf.urls.static import static


app_name="article"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addArticle,name="addArticle"),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateArticle,name="update"),
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('comment/<int:id>',views.addComment,name="comment"),
    path('',views.articles,name="articles"),
]

