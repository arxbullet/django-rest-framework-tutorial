from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Permite al usuario editar su propio perfil"""

    def has_object_permission(self, request, view, obj):
        """Chequear si usuario esta intentado editar su propio perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    '''permite actualizar propio status feed'''
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.user_profile_id == request.user.id
