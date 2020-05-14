from django.urls import path
from . import views
from .views import EntryListView, EntryDetailView,EntryCreateView,EntryUpdateView,EntryDeleteView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about',views.about,name='journal-about'),
    # path('journal',views.journal,name='journal-home'),
    path('journal',EntryListView.as_view(),name='journal-home'),
    path('entry/<int:pk>',EntryDetailView.as_view(),name='entry-detail'),
    path('entry/new',EntryCreateView.as_view(),name='entry-create'),
    path('entry/<int:pk>/update',EntryUpdateView.as_view(),name='entry-update'),
    path('entry/<int:pk>/delete',EntryDeleteView.as_view(),name='entry-delete'),
]
