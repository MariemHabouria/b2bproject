
from django.contrib import admin
from django.urls import path,include

from accounts.views import login_user, signup, logout_user


from store.views import index, postulerD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
 
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),

    path('product/postuler/', postulerD, name="postuler"),
   
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


