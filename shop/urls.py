from django.urls import path
from .import views
urlpatterns = [
    path('',views.home ,name="home"),
    path('reg/',views.regis,name="reg"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('thanks/',views.thank_page,name="thanks"),
    path('cart/',views.cart_page,name="cart"),
    path('fav_viewpage/',views.fav_viewpage,name="fav_viewpage"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('collection/',views.collect,name="collect"),
    path('collection/<str:fname>',views.collections,name="collections"),
    path('collection/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),#Don't give the backslash because post method cannot take the slash
    path('fav',views.fav_page,name="fav"),
]