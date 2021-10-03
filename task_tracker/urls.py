from .views import PlannedListView, TeamListView, TeamDetailView, FailedListView, FinishedListView, CurrentListView, PlannedDetailView, \
    FailedDetailView, FinishedDetailView, CurrentDetailView
from django.urls import path

urlpatterns = [
    path("teams/", TeamListView.as_view()),
    path("teams/<int:pk>/", TeamDetailView.as_view()),

    path('planned/', PlannedListView.as_view()),
    path('planned/<int:pk>', PlannedDetailView.as_view()),

    path('failed/', FailedListView.as_view()),
    path('failed/<int:pk>', FailedDetailView.as_view()),

    path('finished/', FinishedListView.as_view()),
    path('finished/<int:pk>', FinishedDetailView.as_view()),

    path('current/', CurrentListView.as_view()),
    path('current/<int:pk>', CurrentDetailView.as_view()),
]
