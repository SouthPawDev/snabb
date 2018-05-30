from django.urls import path
from franchises import views

app_name = 'franchises'

urlpatterns = [
    path('', views.FranchiseListView.as_view(), name='list'),
    path('<pk>', views.FranchiseDetailView.as_view(), name='detail'),
    path('create/', views.FranchiseCreateView.as_view(), name='create'),
    path('update/<pk>', views.FranchiseUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.FranchiseDeleteView.as_view(), name='delete')
]
