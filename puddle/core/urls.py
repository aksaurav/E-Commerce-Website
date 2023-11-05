from .views import index, contact
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
