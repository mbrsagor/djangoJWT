from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

router = DefaultRouter()
router.register('contact-list', ContactViewSet)

urlpatterns = router.urls
