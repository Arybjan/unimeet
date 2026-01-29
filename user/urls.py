from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register("users", views.UserViewSet)
router.register("student-profiles", views.StudenProfileViewSet)
router.register("professor-profiles", views.ProfessorViewSet)

urlpatterns = router.urls
