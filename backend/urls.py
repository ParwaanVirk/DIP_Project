from django.urls import path
from django.urls.resolvers import URLPattern
from backend.views import *

urlpatterns = [
    path('TransformerAll/', TransformerAllView.as_view(), name = 'all data'),
    path('Transdata_particular_view/', TransData_Particular_View.as_view(), name = 'trans parameters'), 
]