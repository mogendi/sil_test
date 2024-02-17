from product.views import ProductViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"products", ProductViewset)
urlpatterns = router.urls
