import json
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from discussion_forum.models import ForumDiscussion, ForumReply
from discussion_forum.forms import DiscussionForm, ReplyForm

# Create your views here.
def discussion(req):
    return render(req, 'forum.html')

@login_required(login_url='/login/')
def create_discussion(req):
    context = {
        'form': DiscussionForm()
    }
    return render(req, 'create_discussion.html', context)

@login_required(login_url='/login/')
@csrf_exempt
def post_discussion(req):
    body = req.body
    if req.method == "POST":
        title = req.POST.get("title")
        content = req.POST.get("content")

        try:
            data = json.loads(body)
            if title is None:
                title = data['title']

            if content is None:
                content = data['content']
        except:
            pass

        if title is not None and title != "" and content is not None and content != "":
            obj = ForumDiscussion.objects.create(title=title, content=content, user=req.user)
            return JsonResponse({
                "error": False,
                "message": f"Succesfully create discussion (id: {obj.pk})"
            })

    return HttpResponseBadRequest("Bad request")

def get_discussions(req):
    discussions = ForumDiscussion.objects.all()
    return HttpResponse(serializers.serialize("json", discussions, use_natural_foreign_keys=True), content_type="application/json")

def get_discussion_by_id(req, id):
    try:
        discussion = ForumDiscussion.objects.get(pk=id)
        context = {
            "discussion": discussion,
            "form": ReplyForm()
        }
        return render(req, 'discussion.html', context)

    except:
        return HttpResponseNotFound(f"Discussion not exist (id: {id})")

def get_discussion_replies(req, id):
    try:
        response = {
            "user": req.user.username,
            "replies": []
        }

        discussion = ForumDiscussion.objects.get(pk=id)
        replies = ForumReply.objects.filter(discussion=discussion)
        for reply in replies:
            response["replies"].append({
                "pk": reply.pk,
                "content": reply.content,
                "user": reply.user.username,
                "date": reply.date.strftime("%b. %d, %Y"),
                "replyParentPk": reply.pk,
                "replyingTo": reply.replying_to
            })

        return JsonResponse(response)
    except:
        return HttpResponseNotFound(f"Discussion not exist (id: {id})")

@login_required(login_url='/login/')
@csrf_exempt
def add_discussion_reply(req, id):
    try:
        if req.method == "POST":
            body = req.body
            content = req.POST.get("content")

            try:
                data = json.loads(body)
                if content is None:
                    content = data['content']
            except:
                pass

            if content is not None and content != "":
                discussion = ForumDiscussion.objects.get(pk=id)
                reply = ForumReply.objects.create(content=content, discussion=discussion, user=req.user)

                response = {
                    "error": False,
                    "user": req.user.username,
                    "reply": {
                        "pk": reply.pk,
                        "content": reply.content,
                        "user": reply.user.username,
                        "date": reply.date.strftime("%b. %d, %Y"),
                        "replyParentPk": reply.pk,
                        "replyingTo": reply.replying_to
                    }
                }

                return JsonResponse(response)
        
        return HttpResponseBadRequest("Bad request")
    except:
        return HttpResponseNotFound(f"Discussion not exist (id: {id})")

@login_required(login_url='/login/')
@csrf_exempt
def add_nested_reply(req, id):
    try:
        if req.method == "POST":
            body = req.body
            content = req.POST.get("content")
            user = req.POST.get("user")

            try:
                data = json.loads(body)
                if content is None:
                    content = data['content']

                if user is None:
                    user = data['user']
            except:
                pass

            if content is not None and content != "":
                reply_parent = ForumReply.objects.get(pk=id)
                reply = ForumReply.objects.create(content=content, reply=reply_parent, user=req.user, replying_to=user)

                response = {
                    "error": False,
                    "user": req.user.username,
                    "reply": {
                        "pk": reply.pk,
                        "content": reply.content,
                        "user": reply.user.username,
                        "date": reply.date.strftime("%b. %d, %Y"),
                        "replyParentPk": id,
                        "replyingTo": user
                    }
                }

                return JsonResponse(response)
        
        return HttpResponseBadRequest("Bad request")
    except:
        return HttpResponseNotFound(f"Reply not exist (id: {id})")

def get_nested_replies(req, id):
    try:
        response = {
            "user": req.user.username,
            "replies": []
        }

        reply_parent = ForumReply.objects.get(pk=id)
        replies = ForumReply.objects.filter(reply=reply_parent)
        for reply in replies:
            response["replies"].append({
                "pk": reply.pk,
                "content": reply.content,
                "user": reply.user.username,
                "date": reply.date.strftime("%b. %d, %Y"),
                "replyParentPk": id,
                "replyingTo": reply.replying_to
            })

        return JsonResponse(response)
    except:
        return HttpResponseNotFound(f"Discussion not exist (id: {id})")