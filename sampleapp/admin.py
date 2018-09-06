from django.contrib import admin

from .models import SampleModel
from .models import ForeignKeySampleModel

admin.site.register(SampleModel)
admin.site.register(ForeignKeySampleModel)