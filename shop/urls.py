"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from store import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path('product_details/<str:pname>',views.product_details,name="product_details"),
    path('contact/',views.contact,name='contact'),
    path('comunication',views.comunication,name='comunication'),
    path('childs/',views.childs,name='childs'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women'),
    path('adventures/',views.adventures,name='adventures'),
    path('order',views.order,name='order'),
    path('buys/<str:bname>/',views.buys,name='buys'),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('login/',views.login_page,name="login"),
    path('register/',views.register,name='register'),
    path('logout',views.logout_page,name="logout"),

    

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

