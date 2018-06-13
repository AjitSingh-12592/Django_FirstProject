# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from first_app.models import Topic,Webpage,AccessRecord

# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
