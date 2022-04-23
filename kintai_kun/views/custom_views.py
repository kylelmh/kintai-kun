from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from django.views import View

class UserView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)
  
class StaffView(View):
  @method_decorator(staff_member_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

class ViewHelpers():
  @login_required
  def employee_change_password(request):
    if request.method == 'POST':
      form = PasswordChangeForm(request.user, request.POST)
      if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)  # Important!
        messages.success(request, 'パスワード変更されました。')
        return redirect('employee_change_password')
      else:
        messages.error(request, 'エラーが発生しました。')
    else:
      form = PasswordChangeForm(request.user)
    return render(request, 'main/password_change.html', {
      'form': form
    })