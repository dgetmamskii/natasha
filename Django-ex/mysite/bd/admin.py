from django.contrib import admin
from .models import Inn
from .models import NCoast
from .models import NCont
from .models import Fio
from .models import DateCoast
from .models import DateCont
from .models import Org
from .models import Money

admin.site.register(Inn)
admin.site.register(NCoast)
admin.site.register(NCont)
admin.site.register(Fio)
admin.site.register(DateCoast)
admin.site.register(DateCont)
admin.site.register(Org)
admin.site.register(Money)
