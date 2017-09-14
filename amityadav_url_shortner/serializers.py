from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.conf import settings
from amityadav_url_shortner.services import convert_to_base_62
from utils.misc import is_valid_url
from .models import WebUrl


class WebUrlSerializer(serializers.Serializer):
    def create(self, validated_data):
        obj, _ = WebUrl.objects.get_or_create(**validated_data)
        return obj

    def to_representation(self, instance):
        return {
            'shorten_url': settings.DOMAIN_NAME + "/" + convert_to_base_62(instance.id)
        }

    def to_internal_value(self, data):
        url = data.get('url')

        if not url:
            raise ValidationError({
                'url': 'This field is required.'
            })

        if not is_valid_url(url):
            raise ValidationError({
                'url': 'The given field is not valid'
            })

        return {
            'url': url
        }
