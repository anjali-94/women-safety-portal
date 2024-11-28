from django.contrib import admin
from auth_app.models import Story
from auth_app.models import UserRegistration
from auth_app.models import Complaint
from auth_app.models import Feedback


# Register your models here.
admin.site.register(Story)
admin.site.register(UserRegistration)
admin.site.register(Complaint)
admin.site.register(Feedback)




