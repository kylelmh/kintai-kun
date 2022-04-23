from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View

class UserView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)