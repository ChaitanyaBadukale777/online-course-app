from datetime import date
def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(#<HINT> add today here#)
    return HttpResponse(content=#<HINT> use the template object as argument value#)