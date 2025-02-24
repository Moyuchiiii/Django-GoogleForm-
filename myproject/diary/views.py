from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import PageForm
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
            ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(
            request, "diary/index.html", {"datetime_now": datetime_now}
            )
    
class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "diary/page_form.html", {"form": form})
    
    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("diary:index")
        return render(request, "diary/page_form.html", {"form": form})

class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.filter(answertf=False).order_by("-page_date")
        return render(request, "diary/page_list.html", {"page_list": page_list})
    
class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_detail.html", {"page": page})
    
class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(instance=page)
        return render(request, "diary/page_update.html", {"form": form})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("diary:page_detail", id=id)
        return render(request, "diary/page_update.html", {"form": form})
    
class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_confirm_delete.html", {"page": page})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return redirect("diary:page_list")

class PageAnswerView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_answer.html", {"page": page})
    
    def post(self, request, id):
        original_page = get_object_or_404(Page, id=id)
        new_page = Page(
            original_page=original_page,
            answered_by=request.user,
            title=f"{original_page.title}の回答 {request.user}",
            
            **{f"q{i}": getattr(original_page, f"q{i}") for i in range(1, 11)},
            **{f"a{i}": getattr(original_page, f"q{i}") for i in range(1, 11)},
            answertf=True
        )
        new_page.save()
        return redirect("diary:page_list")

def signin(request):
    return render(request, 'signin.html')

class PageAnswerListView(LoginRequiredMixin, View):
    def get(self, request, id):
        page_list = Page.objects.filter(answertf=True, original_page__id=id).order_by("-page_date")
        return render(request, "diary/page_answer_list.html", {"page_list": page_list})
    
class PageAnswerCheckView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_answer_check.html", {"page": page})

index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
page_answer = PageAnswerView.as_view()
page_answer_list = PageAnswerListView.as_view()
page_answer_check = PageAnswerCheckView.as_view()