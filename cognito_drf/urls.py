from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .notes.views import NoteViewSet
from .oauth.views import OAuthCallbackView, OAuthLoginView

router = SimpleRouter()
router.register("notes", NoteViewSet, basename="note")

urlpatterns = [
    path('api/', include(router.urls)),
    path('oauth/login/', OAuthLoginView.as_view()),
    path('oauth/callback/', OAuthCallbackView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
