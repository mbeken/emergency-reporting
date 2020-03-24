from .subscription import BaseSubscription
from .product import (
    AgencyIncidentsProduct,
    AgencyAdministrationProduct,
    AgencyClassesProduct
    )


class EmergencyReportingClient():

    def __init__(self, client_id=None, client_secret=None, username=None, password=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.AgencyIncidentsProduct = AgencyIncidentsProduct(
            BaseSubscription(
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                password=password
                )
            )
        self.AgencyAdministrationProduct = AgencyAdministrationProduct(
            BaseSubscription(
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                password=password
                )
        )
        self.AgencyClassesProduct = AgencyClassesProduct(
            BaseSubscription(
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                password=password
                )
        )

    def auth(self):
        self.AgencyIncidentsProduct.subscription.Auth.get_token()
        self.AgencyAdministrationProduct.subscription.Auth.get_token()
        self.AgencyClassesProduct.subscription.Auth.get_token()
        