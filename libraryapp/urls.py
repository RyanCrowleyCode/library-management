# This is a lot like the ApplicationViews we used in React.
# We are defining what view the user will be served up based on the url

from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', book_list, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', list_librarians, name='librarians'),
    path('libraries/', list_libraries, name='libraries')
]