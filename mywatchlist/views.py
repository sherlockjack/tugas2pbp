from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers
# TODO: Create your views here.
def show_mywatchlist(request):
    data_barang_film = WatchlistItem.objects.all()
    context = {
    'list_film': data_barang_film,
    'Name': 'Reiou Nagata',
    'ID': '2106636943'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request,id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request,id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_html_by_id(request,id):
    data_barang_film = WatchlistItem.objects.filter(pk=id)
    context = {
    'list_film': data_barang_film,
    'Name': 'Reiou Nagata',
    'ID': '2106636943'
    }
    return render(request, "mywatchlist.html", context)


def show_html(request):
    data_barang_film = WatchlistItem.objects.all()
    context = {
    'list_film': data_barang_film,
    'Name': 'Reiou Nagata',
    'ID': '2106636943'
    }
    return render(request,"mywatchlist.html",context)