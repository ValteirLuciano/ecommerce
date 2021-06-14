from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf import settings

from accounts.views import login_page, register_page, logout_page

urlpatterns = [
    path('', include('core.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', include("carts.urls", namespace="cart")),

    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
