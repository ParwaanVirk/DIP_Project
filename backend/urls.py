from django.urls import path
from django.urls.resolvers import URLPattern
from backend.views import *

urlpatterns = [
    path('TransformerAll/', TransformerDataAll, name = 'all data'),
    path('TransformerLoc/', TransformerLocality, name = 'lim data'),
    path('Transformer_by_ID/', TransformerByID, name = 'by id'),
    path('TransformerIDS/', TransformerIDS, name = 'all id'),


]