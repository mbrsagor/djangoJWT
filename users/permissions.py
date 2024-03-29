from rest_framework import permissions


class PermissionHelperMixin(object):
    def admin_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAdminUser()]
        else:
            return []

    def authenticated_user_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        else:
            return []
