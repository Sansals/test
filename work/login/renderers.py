import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # Отображаем данные пользователя в простанстве имен 'user'.
        return json.dumps({
            'user': data
        })