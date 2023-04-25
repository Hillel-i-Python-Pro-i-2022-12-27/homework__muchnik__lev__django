from django.views.generic import ListView, TemplateView

from apps.middleware_counter.models import RequestLog

from django.contrib.sessions.backends.cached_db import SessionStore
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class LogsListView(ListView):
    paginate_by = 30
    model = RequestLog
    template_name = "middleware_counter/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = RequestLog.objects.all().order_by("-id")
        paginator = Paginator(context["object_list"], self.paginate_by)

        page = self.request.GET.get("page")

        try:
            context["object_list"] = paginator.page(page)
        except PageNotAnInteger:
            context["object_list"] = paginator.page(1)
        except EmptyPage:
            context["object_list"] = paginator.page(paginator.num_pages)

        count_logs = RequestLog.objects.count()
        context["title"] = "List"
        context["count_logs"] = count_logs
        return context


class SessionsListView(ListView):
    paginate_by = 30
    model = RequestLog
    template_name = "middleware_counter/list_sessions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        session: SessionStore = self.request.session
        session_id = session.session_key

        context["object_list"] = RequestLog.objects.filter(session_id=session_id).order_by("-id")
        paginator = Paginator(context["object_list"], self.paginate_by)

        page = self.request.GET.get("page")

        try:
            context["object_list"] = paginator.page(page)
        except PageNotAnInteger:
            context["object_list"] = paginator.page(1)
        except EmptyPage:
            context["object_list"] = paginator.page(paginator.num_pages)

        count_logs = RequestLog.objects.filter(session_id=session_id).order_by("-id").count()
        context["title"] = "List"
        context["count_logs"] = count_logs
        return context


class UserListView(TemplateView):
    model = RequestLog
    template_name = "middleware_counter/list_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["object_list"] = RequestLog.objects.filter().order_by("-id")
        page = self.request.GET.get("page")

        paginator = Paginator(context["object_list"], 30)

        try:
            context["object_list"] = paginator.page(page)
        except PageNotAnInteger:
            context["object_list"] = paginator.page(1)
        except EmptyPage:
            context["object_list"] = paginator.page(paginator.num_pages)

        count_logs = RequestLog.objects.filter().order_by("-id").count()
        context["title"] = "List"
        context["count_logs"] = count_logs
        return context
