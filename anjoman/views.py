# from django.shortcuts import render
# from .models import Member

# def score_view(request):
#     members = Member.objects.all()
#     members_data = [
#         {
#             'name': member.firstname,
#             'lname': member.lastname,
#             'score': member.score
#         }
#         for member in members
#     ]
#     return render(request, 'members.html', {'members': members_data})
from django.shortcuts import render
from .models import Member

from django.shortcuts import render
from .models import Member

def score_view(request):
    search_query = request.GET.get('search')
    members = Member.objects.all()

    if search_query:
        # Change 'name__icontains' to 'firstname__icontains'
        members = members.filter(firstname__icontains=search_query)

    sort_by = request.GET.get('sort')
    if sort_by:
        if sort_by == 'name':
            # Change 'name' to 'firstname'
            members = members.order_by('firstname')
        elif sort_by == 'lname':
            members = members.order_by('lastname')
        elif sort_by == 'score':
            members = members.order_by('score')

    members_data = [
        {
            'name': member.firstname,
            'lname': member.lastname,
            'score': member.score
        }
        for member in members
    ]
    return render(request, 'members.html', {'members': members_data})
