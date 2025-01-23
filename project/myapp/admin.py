from django.contrib import admin

# Register your models here.
# user_login, user_details,pic_pool , location_master , category_master
# user_search_history , general_news 

from .models import user_login, user_details

from.models import pic_pool , location_master , category_master
from.models import user_search_history , general_news 


admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(pic_pool)
admin.site.register(location_master)
admin.site.register(category_master)
admin.site.register(user_search_history)
admin.site.register(general_news )