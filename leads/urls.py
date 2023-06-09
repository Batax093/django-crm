from django.urls import path

from .views import (
    LeadListView, 
    LeadDetailView,
    LeadCreateView, 
    LeadUpdateView, 
    LeadDeleteView, 
    AssignAgentView,
    CategoryListView,
    CategoryDetailView,
    LeadCategoryUpdateView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryUpdateView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-customer/', AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/tugas/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('list-tugas/', CategoryListView.as_view(), name='category-list'),
    path('list-tugas/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('list-tugas/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('list-tugas/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('buat-tugas/', CategoryCreateView.as_view(), name='category-create'),
]
