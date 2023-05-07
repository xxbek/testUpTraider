from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, DashboardForm, PointForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Dashboard, TreePoint, TreePointRelation


def index(request):
    dashboard_list = Dashboard.objects.order_by("id").all()
    paginator = Paginator(dashboard_list, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request,
                  'index.html',
                  {"page": page,
                   'paginator': paginator}
                  )


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    form.error_messages = 'fvf'
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


@login_required
def new_dashboard(request):
    if request.method == 'POST':
        form = DashboardForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dashboard = form.save(commit=False)
            dashboard.user_id = request.user
            dashboard.save()
            messages.info(request, f"Dashboard {name} is created.")
            return redirect("index")
        else:
            messages.error(request, "Invalid dashboard form.")

    form = DashboardForm()
    return render(request=request, template_name="dashboard_new.html", context={"dashboard_form": form})


@login_required()
def dashboard_view(request, dashboard_id):
    dashboard = get_object_or_404(Dashboard, id=dashboard_id)
    points = TreePoint.objects.filter(dashboard_id=dashboard_id)
    root_points = [point for point in points if point.parent_id is None]
    relations = [point for point in TreePointRelation.objects.all() if point.point_id in points]
    return render(
        request=request,
        template_name="dashboard_view.html",
        context={"dashboard": dashboard, "points": points, "root_points": root_points, "relations": relations}
    )


@login_required
def dashboard_delete(request):
    pass


def _create_relation(parent_id, child_id):
    child = get_object_or_404(TreePoint, id=child_id)
    relation = TreePointRelation(point_id=parent_id, child_id=child)
    relation.save()


@login_required
def point_create(request, dashboard_id):
    if request.method == 'POST':
        point_form = PointForm(data=request.POST)
        if point_form.is_valid():
            dashboard = get_object_or_404(Dashboard, id=dashboard_id)
            point = point_form.save(commit=False)
            point.dashboard_id = dashboard
            point.user_id = request.user
            point.save()
            messages.info(request, f"Point `{point}` is created.")
            if point.parent_id is not None:
                _create_relation(point.parent_id, point.id)
            return redirect("dashboard_view", dashboard_id)
        else:
            messages.error(request, "Invalid point form.")

    point_form = PointForm(dashboard_id=dashboard_id)
    return render(request=request, template_name="point_new.html", context={"point_form": point_form, "dashboard_id": dashboard_id})


@login_required
def point_delete(request, dashboard_id):
    pass



