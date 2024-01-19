from django.urls import path
from.import views
from.views import logout_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.store,name='store'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('adminproductlist/',views.adminproductlist,name='adminproductlist'),
    path('store/',views.store,name='store'),
    path('adminproductcreate/',views.adminproductcreate,name='adminproductcreate'),
    path('submitproduct/',views.submitproduct,name='submitproduct'),
    path('userproductdetails/<int:product_id>/',views.userproductdetails,name='userproductdetails'),
    # path('userpurchase/',views.userpurchase,name='userpurchase'),
    path('logout/',logout_view,name='logout'),
    path('bookproduct/<int:product_id>/', views.bookproduct, name='bookproduct')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)