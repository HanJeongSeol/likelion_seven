from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
import accountapp.views
# media 사용하기위해서 아래 두 개를 import해온다.
from django.conf import settings    
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home,name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio/',portfolio.views.portfolio,name='portfolio'),
    path('account/',include('accountapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)