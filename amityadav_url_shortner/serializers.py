from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from amityadav_url_shortner.services import convert_to_base_62, convert_to_base_10
from utils.misc import is_valid_url
from .models import WebUrl


class WebUrlShortnerSerializer(serializers.Serializer):
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


class WebUrlExpanderSerializer(serializers.Serializer):
    url = serializers.URLField()

    def to_representation(self, instance):
        url = instance
        encoded_hash = url.split("/")[-1]
        db_id = convert_to_base_10(encoded_hash)
        try:
            web_url_obj = WebUrl.objects.get(id=db_id)
            expanded_url = web_url_obj.url
        except WebUrl.DoesNotExist:
            raise ValidationError("URL %s does not exists in out database" % url)

        return {
            'url': expanded_url
        }
