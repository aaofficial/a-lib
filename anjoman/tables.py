import django_tables2 as tables
from .models import Member

class MemberTable(tables.Table):
    class Meta:
        model = Member
        # template_name = "django_tables2/bootstrap4.html"
        fields = ("firstname", "lastname", "score")
        attrs = {"class": "table"}

