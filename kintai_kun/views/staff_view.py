from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.views import View

class StaffView(View):
  @method_decorator(staff_member_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)