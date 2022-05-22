from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateAdopts(request, adopt, results):
    page = request.GET.get('page')
    paginator = Paginator(adopt, results)

    try:
        adopt = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        adopt = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        adopt = paginator.page(page)

    leftIndex = (int(page) - 2)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, adopt

def paginateLosts(request, lost, results):
    page = request.GET.get('page')
    paginator = Paginator(lost, results)

    try:
        lost = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        lost = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        lost = paginator.page(page)

    leftIndex = (int(page) - 2)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, lost

def paginateFoundeds(request, founded, results):
    page = request.GET.get('page')
    paginator = Paginator(founded, results)

    try:
        founded = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        founded = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        founded = paginator.page(page)

    leftIndex = (int(page) - 2)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, founded