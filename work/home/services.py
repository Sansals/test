from .models import Rules
from forum.models import Articles
import logging
import datetime

from work.global_services import get_username

logger = logging.getLogger(__name__)


def get_rules_all(request):
    """Берёт все объекты таблицы Rules, сортирует их по ID записи"""
    try:
        all_rules = Rules.objects.order_by('rule_id')
        logger.info(f'{datetime.datetime.now()} |INFO| Username: {get_username(request)} | User get all objects from home.Rules')
    except ValueError:
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |home.services|'
            f'ValueError in get all objects from home.Rules')
    except Exception:
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |home.services|'
            f'Exception in get all objects from home.Rules')
    return all_rules

def get_all_articles(request):
    """Берёт все объекты таблицы Articles, сортирует их по дате"""
    try:
        logger.info(
            f'{datetime.datetime.now()} |INFO| '
            f'Username: {get_username(request)} |'
            f' |home.services|'
            f'User get all objects from addlist.Articles')

        return Articles.objects.order_by('-date')

    except ValueError:
        logger.warning(
            f'{datetime.datetime.now()} |Warning| '
            f'Username: {get_username(request)} |'
            f' |home.services|'
            f'ValueError: User cant get all objects from addlist.Articles')
        pass
    except Exception:
        logger.warning(
            f'{datetime.datetime.now()} |Warning| '
            f'Username: {get_username(request)} |'
            f' |home.services|'
            f'Exception: User cant get all objects from addlist.Articles')
        pass