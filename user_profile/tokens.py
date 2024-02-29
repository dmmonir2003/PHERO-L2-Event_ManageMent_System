from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.crypto import constant_time_compare
from django.utils.http import base36_to_int, int_to_base36


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Generate a hash value containing the user's primary key and email, to be used in the token.
        """
        return (
            str(user.pk) + user.email + str(timestamp)
        )


account_activation_token = AccountActivationTokenGenerator()
