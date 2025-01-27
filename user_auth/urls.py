from django.urls import path
from user_auth.views import user_signup, user_login, user_logout

urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    # এখানে সঠিকভাবে 'UserProfile' ব্যবহার করুন
]
