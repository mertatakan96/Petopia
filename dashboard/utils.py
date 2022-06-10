from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateBlogs(request, blogs, results):
    page = request.GET.get('page')
    paginator = Paginator(blogs, results)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blogs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        blogs = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, blogs

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

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, forums

def paginatePetlovers(request, pet_lover_accounts, results):
    page = request.GET.get('page')
    paginator = Paginator(pet_lover_accounts, results)

    try:
        pet_lover_accounts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        pet_lover_accounts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        pet_lover_accounts = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, pet_lover_accounts

def paginateBusiness(request, business_accounts, results):
    page = request.GET.get('page')
    paginator = Paginator(business_accounts, results)

    try:
        business_accounts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        business_accounts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        business_accounts = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, business_accounts

def paginateFounded(request, founded, results):
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

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, founded

def paginateAdopted(request, adopted, results):
    page = request.GET.get('page')
    paginator = Paginator(adopted, results)

    try:
        adopted = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        adopted = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        adopted = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, adopted

def paginateLost(request, lost, results):
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

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, lost