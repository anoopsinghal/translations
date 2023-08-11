import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer
from .models import Article

class ArticleViews(APIView):
    def saveLangString(self, data) -> bool:
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return True
        # end if

        return False

    # end saveLangString

    def post(self, request):
        transjson = request.data
        print(transjson)

        # get md5hash of the first string to tie both entries together
        md5hash = hashlib.md5(transjson['fromStr'].encode('utf-8')).hexdigest()

        result = self.saveLangString({"md5hash": md5hash, "langCode": transjson['fromLang'], "article": transjson["fromStr"]})
        if result:
            result = self.saveLangString({"md5hash": md5hash, "langCode": transjson['toLang'], "article": transjson["toStr"]})
        # end if                    ]

        if result:
            return Response({"status": "success", "data": transjson}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "errored out"}, status=status.HTTP_400_BAD_REQUEST)
