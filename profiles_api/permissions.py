from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ ALLOWS USER TO EDIT THEIR OWN PROFILE """

    def has_object_permission(self,request,view,obj):
        """ CHECK USER IS TRYING TO EDIT THEIR OWN PROFILE """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id 