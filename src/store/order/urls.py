from order.views import OrderViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"orders", OrderViewset)
urlpatterns = router.urls
