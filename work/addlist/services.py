from .models import Articles
from django.views.generic import DetailView
import logging
import datetime


logger = logging.getLogger(__name__)

class NewsDatailView(DetailView):
    try:
        model = Articles
        template_name = 'addlist/details_view.html'
        context_object_name = 'article'
    except ValueError:
        logger.warning(f'{datetime.datetime.now()} Не удалось получить объекты/объекты отсутствуют в addlist.Articles')
    except Exception:
        logger.error(f'{datetime.datetime.now()} Неизвестная ошибка при работе с addlist.Articles. Файл addlist.services')