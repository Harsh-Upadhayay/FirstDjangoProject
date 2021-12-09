#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:11:55 2021

@author: harsh
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]