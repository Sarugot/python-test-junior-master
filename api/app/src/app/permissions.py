from rest_framework import permissions

from .utils import get_client_ip


class AlgorithmPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        ip = get_client_ip(request)
        lst = list(map(int, ip.replace('.', '')))
        odds = [i for i in lst if i % 2]
        evens = [i for i in lst if not i % 2]
        return len(odds) == len(evens)
