#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-21 22:08:37 (CST)
# Last Update:星期三 2017-1-25 21:48:26 (CST)
#          By:
# Description:
# **************************************************************************
from flask import render_template, g, redirect, url_for
from common.views import BaseMethodView as MethodView
from api.topic.models import Topic, Collect
from api.reply.models import Reply
from api.user.models import User


class UserTopicListView(MethodView):
    def get(self):
        username = g.username
        page, number = self.page_info
        filter_dict = {'author__username': username}
        user = User.get(username=username)
        topics = Topic.get_list(page, number, filter_dict)
        data = {'topics': topics, 'user': user}
        return render_template('mine/topic_list.html', **data)


class UserReplyListView(MethodView):
    def get(self):
        username = g.username
        page, number = self.page_info
        filter_dict = {'author__username': username}
        replies = Reply.get_list(page, number, filter_dict)
        user = User.get(username=username)
        data = {'replies': replies, 'user': user}
        return render_template('mine/reply_list.html', **data)


class UserCollectListView(MethodView):
    def get(self):
        username = g.username
        page, number = self.page_info
        filter_dict = {'author__username': username}
        collects = Collect.get_list(page, number, filter_dict)
        user = User.get(username=username)
        data = {'collects': collects, 'user': user}
        return render_template('mine/collect_list.html', **data)


class UserFollowerListView(MethodView):
    def get(self):
        username = g.username
        user = User.get(username=username)
        page, number = self.page_info
        users = user.following_users.paginate(page, number, True)
        data = {'users': users, 'user': user}
        return render_template('mine/follower_list.html', **data)


class UserFollowingListView(MethodView):
    def get(self):
        return redirect(url_for('follow.topic'))
        # username = g.username
        # page, number = self.page_info
        # filter_dict = {'followers__username': username}
        # users = User.get_list(page, number, filter_dict)
        # user = User.get(username=username)
        # data = {'users': users, 'user': user}
        # return render_template('mine/following_list.html', **data)
