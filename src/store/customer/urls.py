from customer.views import CustomerViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"customers", CustomerViewset)
urlpatterns = router.urls
