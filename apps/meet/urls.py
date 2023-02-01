from rest_framework.routers import DefaultRouter


from .views import QuestionnaireViewSet, LikeViewSet, PhotoViewSet

router = DefaultRouter()
router.register('questionnnaire',QuestionnaireViewSet,basename='questionnaire')
router.register('like',LikeViewSet,basename='like')
router.register('photo', PhotoViewSet, basename='photo')

urlpatterns = router.urls