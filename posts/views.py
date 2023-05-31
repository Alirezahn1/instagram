from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User

from django.views import View
from django.db.models import Q
from posts.models import Follow, Stream, Post
from profiles.models import Profile


class HomeView(View):
    def get(self, request):
        user = request.user
        # all_users = User.objects.all()
        # follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

        # profile = Profile.objects.all()

        posts = Stream.objects.filter(user=user.id)
        group_ids = []

        for post in posts:
            group_ids.append(post.post_id)

        post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

        # query = request.GET.get('q')
        # if query:
        #     users = User.objects.filter(Q(username__icontains=query))
        #
        #     paginator = Paginator(users, 6)
        #     page_number = request.GET.get('page')
        #     users_paginator = paginator.get_page(page_number)

        context = {
            'post_items': post_items,
            # 'follow_status': follow_status,
            # 'profile': profile,
            # 'all_users': all_users,
            # 'users_paginator': users_paginator,
        }
        return render(request, 'base/home.html',context)
