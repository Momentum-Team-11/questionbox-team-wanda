"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views as api_views
from api.serializers import QuestionSerializer, QuestionAnswerSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    path('api/questions/', api_views.QuestionListView.as_view(), name="api-question"),  #this is a list of questions, similar to homepage on habittrack
    path('api/profile/myquestions', api_views.UserQuestionsListView.as_view(), name="api-userquestions"), #this is questions a user has asked
    path('api/<int:pk>/answers', api_views.AnswerListView.as_view(), name='questions_answer'), #this is all answers for one question
    
]
