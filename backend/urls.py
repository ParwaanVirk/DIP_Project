from django.urls import path
from django.urls.resolvers import URLPattern
from backend.views import *

urlpatterns = [
    path('TransformerAll/', TransformerDataAll, name = 'all data'),
    path('TransformerLoc/', TransformerLocality, name = 'lim data'),
    
]