from django.urls import include, path
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from users.views import UsersViewSet, PatientViewSet, PatientNextOfKeenViewSet, TriadViewSet, SummaryStatisticsViewSet

router = nested_routers.DefaultRouter()
router.register(prefix='patients', viewset=PatientViewSet, basename='patients')
router.register(prefix='summary', viewset=SummaryStatisticsViewSet, basename='summary')
router.register(prefix='', viewset=UsersViewSet, basename='users')
next_of_keen = nested_routers.NestedDefaultRouter(router, r'', lookup='patient')
next_of_keen.register(prefix=r'next-of-keen', viewset=PatientNextOfKeenViewSet, basename='next-of-keen')

triad = nested_routers.NestedDefaultRouter(router, r'', lookup='patient')
triad.register(prefix='triads', viewset=TriadViewSet, basename='triads')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(next_of_keen.urls)),
    path(r'', include(triad.urls))
]
