from django.urls import path
from office import views

app_name = 'office'

urlpatterns = [
    path('', views.OfficeView.as_view(), name='office_index'),
    # PM
    path('pm/', views.PmListView.as_view(), name='pm_list'),
    path('pm/<pk>', views.PmDetailView.as_view(), name='pm_detail'),
    path('pm/create/', views.PmCreateView.as_view(), name='pm_create'),
    path('pm/update/<pk>', views.PmUpdateView.as_view(), name='pm_update'),
    path('pm/delete/<pk>', views.PmDeleteView.as_view(), name='pm_delete'),
    # APM
    path('apm/', views.ApmListView.as_view(), name='apm_list'),
    path('apm/<pk>', views.ApmDetailView.as_view(), name='apm_detail'),
    path('apm/create/', views.ApmCreateView.as_view(), name='apm_create'),
    path('apm/update/<pk>', views.ApmUpdateView.as_view(), name='apm_update'),
    path('apm/delete/<pk>', views.ApmDeleteView.as_view(), name='apm_delete')
]
