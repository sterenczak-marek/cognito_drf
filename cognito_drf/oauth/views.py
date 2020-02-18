import logging

from django.conf import settings
from oauthlib.oauth2 import OAuth2Error
from requests_oauthlib import OAuth2Session
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

default_scope = ["email", "profile", "openid"]
SESSION_STATE_KEY = "oauth_state"
SESSION_TOKEN_KEY = "oauth_token"

logger = logging.getLogger(__file__)


class OAuthCallbackView(APIView):
    """
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        cognito = OAuth2Session(
            settings.COGNITO_CLIENT_ID,
            redirect_uri=get_client_redirect_uri(request),
            state=request.session[SESSION_STATE_KEY],
        )
        try:
            token = cognito.fetch_token(
                settings.COGNITO_TOKEN_URL,
                client_secret=settings.COGNITO_CLIENT_SECRET,
                authorization_response=request.build_absolute_uri(),
            )

        except OAuth2Error as e:
            logger.warning(e)
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)

        request.session[SESSION_TOKEN_KEY] = token
        return Response(token)


class OAuthLoginView(APIView):
    """
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        cognito = OAuth2Session(
            client_id=settings.COGNITO_CLIENT_ID,
            redirect_uri=get_client_redirect_uri(request),
            scope=default_scope,
        )
        authorization_url, state = cognito.authorization_url(settings.COGNITO_AUTHORIZE_URL)
        request.session[SESSION_STATE_KEY] = state

        return Response(status=status.HTTP_302_FOUND, headers={
            "Location": authorization_url,
        })


def get_client_redirect_uri(request):
    return request.build_absolute_uri("/oauth/callback/")
