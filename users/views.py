# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, RedirectView, UpdateView, FormView
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from users.forms import AvatarForm, SignupForm
from users.serializers import UserSerializer
from .models import User, Profile


class UserDetailView(View):
    def get(self, request, username, page):
        context = dict()
        user = User.objects.get(username=username)
        context['user'] = user
        return render(request, 'pages/users/user_detail.html', context=context)

    def post(self, request, username):
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.avatar = form.cleaned_data['avatar']
            profile.save()
        return HttpResponseRedirect(reverse('users:detail', kwargs={'username': username}))


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the usdr making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(request.user,
                                           context={'request': request}).data)
        return super(UserViewSet, self).retrieve(request, pk)


class SettingsView(View):
    def get(self, request):
        return render(request, 'pages/users/settings/settings.html', context=self.get_context_data())

    def get_context_data(self):
        return dict()


# class SignupView(allauth.SignupView):
#     template_name = 'account/signup.html'
#     # form_class = SignupForm
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.GET.get('next') == '/signals/':
#             messages.add_message(request, messages.INFO, "Sign up to add a signal")
#         return super(SignupView, self).dispatch(request, *args, **kwargs)
#
#     # def get_success_url(self):
#         # next_url = self.request.POST.get('next', None)  # here method should be GET or POST.
#         # if next_url:
#         #     return "%s" % (next_url)  # you can include some query strings as well
#         # else:
#         #     return reverse('home')
#         #


class SignupView(FormView):
    template_name = 'account/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        valid = super(SignupView, self).form_valid(form)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        User.objects.create_user(email=email, password=password)
        user = authenticate(username=email, password=password)
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return valid

    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('next') == '/signals/':
            messages.add_message(request, messages.INFO, "Sign up to add a signal")
        return super(SignupView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        next_url = self.request.POST.get('next', None)  # here method should be GET or POST.
        if next_url:
            return "%s" % (next_url)  # you can include some query strings as well
        else:
            return reverse('home')
