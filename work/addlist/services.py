from .models import Articles
from django.views.generic import DetailView

class NewsDatailView(DetailView):
    try:
        model = Articles
        template_name = 'addlist/details_view.html'
        context_object_name = 'article'
    except ValueError:
        pass #logging
    except Exception:
        pass #logging