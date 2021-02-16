from django.urls import path
import shop.views as v
urlpatterns = [
    path("", v.index),
    path("about/", v.about)

]