from views import *
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('user', CustomAuthToken, base_name ='user_api')