from rest_framework.routers import DefaultRouter
from .views_api import EventViewSet, AttendeeViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
