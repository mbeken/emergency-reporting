from .auth import Auth


class BaseSubscription():

    def __init__(
            self, client_id, client_secret,
            username, password, er_aid, er_uid,
            primary_key=None, secondary_key=None):
        self.Auth = Auth(client_id, client_secret, username, password, er_aid, er_uid)
        self.Auth.primary_key = primary_key
