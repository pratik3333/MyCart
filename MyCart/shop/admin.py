from django.contrib import admin

# Register your models here.
from .models import product
admin.site.register(product)

from .models import Location
admin.site.register(Location)

from .models import User
admin.site.register(User)

from .models import Participant
admin.site.register(Participant)