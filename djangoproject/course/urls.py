
from django.urls import path
from course.views import learn_django, learn_python, if_tag_example, for_loop_example, for_dict_example

urlpatterns = [
    path('learndj/', learn_django),
    path('learnpy/', learn_python),
    path('iftag/', if_tag_example),
    path('for/', for_loop_example),
    path('fordict/', for_dict_example)
    
]