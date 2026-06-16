from django.http import JsonResponse
from UserServices.models import ModuleUrls, UserPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication
import re
from django.db.models import Q


class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        current_url = request.path

        # Public URLs that should NOT require JWT token
        public_urls = [
            '/api/auth/login/',
            '/api/auth/signup/',
            '/api/auth/publicApi/',
        ]

        if current_url in public_urls:
            return response

        if current_url in urlToSkip():
            return response

        jwt_auth = JWTAuthentication()

        try:
            auth_result = jwt_auth.authenticate(request)

            if auth_result is None:
                return JsonResponse(
                    {'message': 'Unauthorized'},
                    status=401
                )

            user, token = auth_result

        except Exception:
            return JsonResponse(
                {'message': 'Unauthorized'},
                status=401
            )

        # Skip permission checks for Super Admin
        if user.role == 'Super Admin' or user.domain_user_id.id == user.id:
            return response

        module = find_matching_module(current_url)

        if not module:
            return JsonResponse(
                {'message': 'Module not Exist'},
                status=400
            )

        permission = UserPermissions.objects.filter(
            user=user.id,
            module=module.module
        ).first()

        if not permission or permission.is_permission is False:
            return JsonResponse(
                {'message': 'Permission Denied'},
                status=403
            )

        return response


def urlToSkip():
    modules = ModuleUrls.objects.filter(
        module__isnull=True
    ).values_list(
        'url',
        flat=True
    )

    return modules


def find_matching_module(url):
    regex_pattern = re.sub(
        r'\d+',
        '[^\\/]+',
        url.replace('/', '\\/')
    )

    match_pattern = ModuleUrls.objects.filter(
        Q(url__iregex=f'^{regex_pattern}$')
    ).first()

    return match_pattern
