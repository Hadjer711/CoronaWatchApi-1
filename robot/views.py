
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from scraper.twitterScrapping import getTweets
from scraper.googleSearchScrapping import ParseFeed
from scraper import youtubeScraper
from .serializers import *
from .models import *
from notification.models import *
from config import notifArticleTitre, Suj, notifMapTitre, notifRobotTitre, notifVideoUserTitre, notifVidEtRepTitre, GOOGLE_URL


class VeilleViewSet(viewsets.ModelViewSet):
    queryset = Veille.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VeilleSerializer
    url = GOOGLE_URL

    @action(methods=['post', 'get'], detail=False)
    def getData(self, request):
        if(request.method == "GET"):
            feed = ParseFeed(self.url)
            feed.parse()
            getTweets(50)
            youtubeScraper.scrap_youtube_videos()
            data = Veille.objects.all()
            serializers = VeilleSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = VeilleSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()

                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def getTweets(self, request):
        if (request.method == "GET"):
            data = Veille.objects.filter(type="twitter")
            serializers = VeilleSerializer(data, many=True)
            return Response(serializers.data)

    @action(methods=['get'], detail=False)
    def getGoogle(self, request):
        if (request.method == "GET"):
            data = Veille.objects.filter(type="google")
            serializers = VeilleSerializer(data, many=True)
            return Response(serializers.data)

    @action(methods=['get'], detail=False)
    def getYoutube(self, request):
        if (request.method == "GET"):
            data = Veille.objects.filter(type="youtube")
            serializers = VeilleSerializer(data, many=True)
            return Response(serializers.data)

    @action(methods=['put'], detail=True)
    def Supprimer(self, request, pk=None):
        try:
            veille = Veille.objects.get(
                pk=pk)
        except veille.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VeilleSerializerSupprimer(veille, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def Valider(self, request, pk=None):
        try:
            veille = Veille.objects.get(pk=pk)
        except veille.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VeilleSerializerValider(veille, data=request.data)

        if serializer.is_valid():
            serializer.save()
            notification = Notification(
                titre=notifRobotTitre,
                typeNotif=0,
                description=veille.type+" "+veille.description+" "+Suj
            )
            notification.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def getValidate(self, request):
        if (request.method == "GET"):
            data = Veille.objects.filter(valide=True)
            serializers = VeilleSerializer(data, many=True)
            return Response(serializers.data)
