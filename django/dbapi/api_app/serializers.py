from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # translations for all languages are tied together with md5 of english
    md5hash = serializers.CharField(max_length=32)

    # language code
    langCode = serializers.CharField(max_length=4)

    # actual sentence in the given language
    article = serializers.CharField(max_length=2000)

    class Meta:
        model = Article
        fields = ('__all__')