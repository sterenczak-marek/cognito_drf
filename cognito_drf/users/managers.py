from django.contrib.auth.models import UserManager


class CognitoUserManager(UserManager):

    def get_or_create_for_cognito(self, payload):
        cognito_id = payload['sub']

        user, _ = self.get_or_create(
            cognito_id=cognito_id,
            defaults={
                'email': payload['email'],
                'is_active': True,
            },
        )
        return user
