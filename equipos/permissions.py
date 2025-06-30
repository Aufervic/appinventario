from rest_framework import permissions
class IsAsistente(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Asistente").exists()
