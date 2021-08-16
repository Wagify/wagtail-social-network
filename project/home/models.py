from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from django.shortcuts import render


class HomePage(Page):
    intro = models.CharField(max_length=250,default="Introduction Line")
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    def get_context(self,request):
        context = super().get_context(request)
        context['invite_friends'] = self.get_children().type(InviteFriendsPage)
        print(context)
        return context

class FriendInvitation(models.Model):
    email = models.EmailField(max_length=254,blank=True,default=None)


class InviteFriendsPage(Page):

    intro = RichTextField(blank=True,null=True,default="")
    thankyou_page_title = models.CharField(
        max_length=255, help_text="Title text to use for the 'thank you' page",blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('thankyou_page_title'),
    ]

    def serve(self, request):
        from home.forms import FriendInvitationForm

        if request.method == 'POST':
            form = FriendInvitationForm(request.POST)
            if form.is_valid():
                friend_invite = form.save()
                return render(request, 'home/thankyou.html', {
                    'page': self,
                    'flavour': friend_invite,
                })
        else:
            form = FriendInvitationForm()

        return render(request, 'home/invite_friends.html', {
            'page': self,
            'form': form,
        })
