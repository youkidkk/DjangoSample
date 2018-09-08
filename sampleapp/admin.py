from django.contrib import admin

from .models import SampleModel
from .models import ForeignKeySampleModel
from .models import ManyToManyParentModel
from .models import ManyToManyChildModel

admin.site.register(SampleModel)
admin.site.register(ForeignKeySampleModel)
admin.site.register(ManyToManyParentModel)
admin.site.register(ManyToManyChildModel)
