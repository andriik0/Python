from django.views import View
from django.shortcuts import render

blog_name = "John Doe's blog"
post = {
    "text": "My first post",
    "theme": "Easy talk",
    "comments": [
        "My congratulations!!",
        "Looking forward to the second one",
    ],
}


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {"post": post, "blog_name": blog_name}
        return render(request, "blog/index.html", context=context)
