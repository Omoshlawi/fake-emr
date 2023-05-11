from rest_framework import routers

from users.views import UsersViewSet

router = routers.DefaultRouter()
router.register(prefix='patients', viewset=UsersViewSet, basename='patients')
router.register(prefix='', viewset=UsersViewSet, basename='users')

urlpatterns = router.urls
