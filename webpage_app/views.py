from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from webpage_app.forms import ManufacturerNameSearchForm, ManufacturerForm, ManufacturerPublicForm
from webpage_app.models import Purchaser, Manufacturer, BearingType


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

    return render(request, "webpage_app/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "webpage_app/manufacturer_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ManufacturerListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_name_form"] = \
            ManufacturerNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Manufacturer.objects.select_related("responsible_purchaser")
        form = ManufacturerNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class ManufacturerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manufacturer
    queryset = Manufacturer.objects.select_related(
        "responsible_purchaser"
    ).prefetch_related("produce_bearing_type__bearing_category")


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("webpage_app:manufacturer-list")


class ManufacturerPublicCreateView(generic.CreateView):
    model = Manufacturer
    form_class = ManufacturerPublicForm
    success_url = reverse_lazy("webpage_app:index")
    template_name = "webpage_app/manufacturer_public_form.html"


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("webpage_app:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("webpage_app:manufacturer-list")
