from django.shortcuts import render

from webpage_app.models import Purchaser, Manufacturer


def index(request):
    num_purchasers = Purchaser.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visit = request.session.get("num_visit", 0)
    request.session["num_visit"] = num_visit + 1

    context = {
        "num_purchasers": num_purchasers,
        "num_manufacturers": num_manufacturers,
        "num_visit": num_visit + 1,
    }

    return render(request, "pages/index.html", context=context)
