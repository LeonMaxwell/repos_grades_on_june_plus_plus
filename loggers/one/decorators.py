import functools
import logging
import traceback

from django.db import transaction
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def error_response(exception):
    logger.error(f"Error - {str(exception)}, Traceback - {traceback.format_exc()}")
    res = {"errorMessage": str(exception),
           "traceback": traceback.format_exc()}
    return JsonResponse(res, status=200, safe=not isinstance(res, list), json_dumps_params={'ensure_ascii': False})


def base_view(fn):
    """Декоратор для вьюшек, обрабатывает исключения"""
    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_response(e)
    return inner