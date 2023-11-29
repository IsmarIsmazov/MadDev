from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("chairs", views.ChairViewSet, basename='chairs')

# ---------------------------------------------------------------------------------------------------


router.register("category", views.CategoryViewSet, basename='category')


# ---------------------------------------------------------------------------------------------------
router.register('chairoffice', views.ChairOfficeViewSet, basename='chairoffice')
router.register('armchairoffice', views.ArmchairOfficeViewSet, basename='armchairoffice')
router.register('tableoffice', views.TableOfficeViewSet, basename='tableoffice')
router.register('closetoffice', views.ClosetOfficeViewSet, basename='closetoffice')
router.register('armchairgame', views.ArmchairGameViewSet, basename='armchairgame')
router.register('executivearmchair', views.ExecutiveArmchairViewSet, basename='executivearmchair')
router.register('childrenarmchair', views.ChildrenArmchairViewSet, basename='childrenarmchair')
router.register('pastchair', views.PartsChairViewSet, basename='pastchair')
# ---------------------------------------------------------------------------------------------------

urlpatterns = router.urls
