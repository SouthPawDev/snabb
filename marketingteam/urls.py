from django.urls import path
from marketingteam import views

app_name = 'marketingteam'

urlpatterns = [
    path('', views.SmrListView.as_view(), name='list'),
    path('<pk>', views.SmrDetailView.as_view(), name='detail'),
    path('create/', views.SmrCreateView.as_view(), name='create'),
    path('update/<pk>', views.SmrUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.SmrDeleteView.as_view(), name='delete')
]
