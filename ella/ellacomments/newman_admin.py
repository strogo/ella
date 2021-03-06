from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ella import newman
from ella.ellacomments.models import CommentOptionsObject

from threadedcomments.models import ThreadedComment
from threadedcomments.admin import ThreadedCommentsAdmin

class CommentOptionsGenericInline(newman.GenericStackedInline):
    ct_field = "target_ct"
    ct_fk_field = "target_id"
    model = CommentOptionsObject

    max_num = 1

class ThreadedCommentsNewmanAdmin(ThreadedCommentsAdmin, newman.NewmanModelAdmin):
    pass

MODELS_WITH_COMMENTS = getattr(settings, 'MODELS_WITH_COMMENTS', ('articles.article', 'galleries.gallery', 'interviews.interview', ))

newman.site.register(ThreadedComment, ThreadedCommentsNewmanAdmin)
newman.site.append_inline(MODELS_WITH_COMMENTS, CommentOptionsGenericInline)

# threadedcomments translations for newman
app, n, vn = _('Threadedcomments'), _('Threaded comment'), _('Threaded comments')
