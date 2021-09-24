from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from django.shortcuts import render
import invitations.utils

# Create your models here.
class FriendInvitation(models.Model):
    email = models.EmailField(max_length=254,blank=True,default=None)


class InviteFriendsPage(Page):
    max_count = 1

    intro = RichTextField(blank=True,null=True,default="")
    thankyou_page_title = models.CharField(
        max_length=255, help_text="Title text to use for the 'thank you' page",blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('thankyou_page_title'),
    ]

    def serve(self, request):

        if request.method == 'POST':
            Invitations = invitations.utils.get_invitation_model()
            try:
                invite_obj = Invitations.objects.get(email = request.POST.get("email"))
                print(invite_obj.email)
            except Invitations.DoesNotExist:
                form = invitations.utils.get_invite_form()()
                invite_obj = form.save(email = request.POST.get("email"))
                print(invite_obj.email)
            invite_obj.send_invitation(request)
            return render(request, 'invites/thankyou.html', {
                    'page': self,
                })
        else:
            form = invitations.utils.get_invite_form()

        return render(request, 'invites/invite_friends.html', {
            'page': self,
            'form': form,
        })
