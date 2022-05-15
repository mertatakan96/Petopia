from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Forum
from django.db.models import Q

def paginateForums(request, forums, results):
    page = request.GET.get('page')
    paginator = Paginator(forums, results)

    try:
        forums = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        forums = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        forums = paginator.page(page)

    leftIndex = (int(page) - 2)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, forums

def searchForums(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    forums = Forum.objects.distinct().filter(
        Q(title__icontains=search_query)
    )

    return forums, search_query