from django.template.loader import render_to_string
from django.template import RequestContext

from zenaida.contrib.feedback import forms
from zenaida.contrib.feedback.settings import CONFIG

def render_feedback_widget(request):
    return render_to_string('feedback/feedback_form.html', {
        'form': forms.FeedbackForm(request=request),
        'config': CONFIG,
    }, context_instance=RequestContext(request))
