from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import jobs.views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', jobs.views.home),
                  path('blog/', include('blog.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
