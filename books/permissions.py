from rest_framework import permissions

class ISAuthorOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    # read only permissions to any request
    if request.method in permissions.SAFE_METHODS:
      return True

    #write only allowed to author
    return obj.author == request.user