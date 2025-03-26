from .models import Rules
from addlist.models import Articles


def get_rules_all():
    """Берёт все объекты таблицы Rules, сортирует их по ID записи"""
    try:
        all_rules = Rules.objects.order_by('rule_id')
        #логи
    except ValueError:
        pass #логи
    except Exception:
        pass #логи
    return all_rules

def get_all_articles():
    """Берёт все объекты таблицы Articles, сортирует их по дате"""
    try:
        return Articles.objects.order_by('-date')
        #loging
    except ValueError:
        pass #loging
    except Exception:
        pass #loging