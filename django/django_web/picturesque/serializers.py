# -*- coding: utf-8 -*-

from picturesque.models import Picturesque, Genre
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

class PicturesqueSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    class Meta:
        model = Picturesque
        fields = ["id", "name", "genre", "date"]