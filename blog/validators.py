# from django.contrib.auth import get_user_model, authenticate
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
#
# User = get_user_model()
#
#
# def validate_password(password):
#     if len(password) < 8:
#         raise ValidationError(_('password is too short'), code='invalid')
#
#
# def validate_username(username):
#     try:
#         User.objects.get(username=username)
#         raise ValidationError(
#             _('this user name is already exist'),
#             code='invalid'
#         )
#     except User.DoesNotExist:
#         return username
#
#
# def validate_user_and_name(username, password):
#     if authenticate(username=username, password=password) is None:
#         raise ValidationError(
#             _('user name or password not exist'),
#             code='invalid'
#         )
