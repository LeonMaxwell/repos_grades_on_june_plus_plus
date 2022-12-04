from django.shortcuts import render
import logging
from .decorators import base_view
from .models import Book
# Create your views here.


logger = logging.getLogger(__name__)


@base_view
def index(request):
    logger.info("Запустилась страница index")
    book = Book()
    book.name = "Новая книга"
    book.save()
    1/0
    return render(request, template_name='one/index.html', context={'hello': "Привет мир"})
