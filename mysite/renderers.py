import json
from rest_framework.renderers import JSONRenderer

class PostJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, render_context=None):
        return json.dumps({'person_data':data},ensure_ascii=False)

    