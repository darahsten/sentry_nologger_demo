import logging
from django.conf import settings
from django.shortcuts import redirect
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)


def trigger_error(request):
    # loggs to sentry
    division_by_zero = 1 / 0


def sentry_logs_error(request):
    # loggs to sentry
    try:
        division_by_zero = 1 / 0
    except Exception:
        capture_exception()
    return redirect('/template_view/')


def sentry_nologs_error(request):
    # does not log to sentry
    try:
        division_by_zero = 1/0
    except Exception as e:
        logger.exception(repr(e))
    return redirect('/template_view/')



urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('sentry-logs-error/', sentry_logs_error),
    path('sentry-nologs-error/', sentry_nologs_error),
    path('template_view/', TemplateView.as_view(template_name='base.html'))

    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


