from django.urls import path
from . import views


app_name = "mypollapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("create/", views.create, name="create"),
    # path("update/<int:question_id>/", views.update, name="update"),
    # path("delete/<int:question_id>/", views.delete, name="delete"),
    # path("search/", views.search, name="search"),
    # path("search/results/", views.search_results, name="search_results"),
    # path("search/results/delete/<int:question_id>/", views.delete, name="delete_search_results"),
    # path("search/results/update/<int:question_id>/", views.update, name="update_search_results"),
    # path("search/results/vote/<int:question_id>/", views.vote, name="vote_search_results"),
    # path("search/results/results/<int:question_id>/", views.results, name="results_search_results"),
    # path("
  
]
