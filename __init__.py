# -*- coding: utf8 -*-
from models import Antimat, Normalizer
from django.conf import settings


Normalizer.init(path=settings.MORPHY_RU_DICT_PATH)