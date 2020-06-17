"""
Get JWT token to access a Cloud Run audience
"""
import argparse
import time

from google.oauth2.id_token import verify_oauth2_token
from google.oauth2.service_account import IDTokenCredentials as IDTokCreds
from google.auth.transport.requests import Request


def get_token(audience, key_file):
    """
    Get the Open ID token given the service account key file and the audience.
    :param audience: URL of the service to be accessed
    :param key_file: Path to the service account key JSON file
    :return: JSON Web Token
    """
    creds = IDTokCreds.from_service_account_file(key_file,
                                                 target_audience=audience)
    creds.refresh(Request())
    return creds.token


def verify_token(encoded_token, audience):
    """
    Verify the token issued by Google OAuth2 server
    :param encoded_token: Encoded Token issued by Google
    :param audience: URL of the service to be accessed
    :return: Nothing
    """
    decoded_token = verify_oauth2_token(encoded_token, Request(), audience)
    if decoded_token['iss'] != 'https://accounts.google.com':
        raise ValueError('Invalid Issuer')
    if decoded_token['exp'] < int(time.time()):
        raise ValueError('Token Expired')


def main():
    """Main Driver Function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--audience', help='Audience', required=True)
    parser.add_argument('--key-file', help='Service Account Key', required=True)
    opts = parser.parse_args()
    id_token = get_token(opts.audience, opts.key_file)
    verify_token(id_token, opts.audience)
    print(id_token)

if __name__ == '__main__':
    main()
