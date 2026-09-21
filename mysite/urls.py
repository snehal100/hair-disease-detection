from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from HD_detection import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.userhome, name="homepage"),
    path("about/", views.about, name="about"),
    path("predictImage/", views.predictImage, name="predictImage"),
    path("alopecia/", views.alopecia_view, name="alopecia"),        # Path for Alopecia view
    path("folliculitis/", views.folliculitis_view, name="folliculitis"),  # Path for Folliculitis view
    path("psoriasis/", views.psoriasis_view, name="psoriasis"),        # Path for Psoriasis view
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),  # Add other paths as needed
    path('index/', views.index, name='index'),
    path("accounts/", include("accounts.urls")),  # Include accounts app URLs

    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
