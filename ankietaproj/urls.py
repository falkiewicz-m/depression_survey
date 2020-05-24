from django.contrib import admin
from django.urls import path
from ankietaapp.views import survey, indexpage, resultsOfSurvey

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ankieta/', survey),
    path('mainpage/', indexpage),
    path('wyniki/', resultsOfSurvey),
]
