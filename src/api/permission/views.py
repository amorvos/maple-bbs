#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-17 09:31:49 (CST)
# Last Update:星期三 2017-1-25 21:46:14 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.serializer import FlaskSerializer as Serializer
from flask_maple.response import HTTPResponse
from common.views import BaseMethodView as MethodView
from .models import Group


class GroupListView(MethodView):
    def get(self):
        page, number = self.page_info
        users = Group.get_list(page, number)
        serializer = Serializer(users, many=True)
        return HTTPResponse(HTTPResponse.NORMAL_STATUS,
                            **serializer.data).to_response()

    def post(self):
        return 'post'


class GroupView(MethodView):
    def get(self, username):
        user = Group.get(username=username)
        serializer = Serializer(user, many=False)
        return HTTPResponse(
            HTTPResponse.NORMAL_STATUS, data=serializer.data).to_response()

    def put(self, username):
        return 'put'

    def delete(self, username):
        return 'delete'
