from .api import (
    AgenyIncidentsApi,
    AgencyUsersApi,
    AgencyStationsApi,
    AgencyClassesApi
    )


class Product():

    def __init__(self, name, path, subscription):
        self.name = name
        self.path = path
        self.subscription = subscription
        self.apis = []


class AgencyIncidentsProduct(Product):

    def __init__(self, subscription):
        super().__init__('Agency Incidents', 'agencyincidents/', subscription)
        self.AgencyIncidentsApi = AgenyIncidentsApi(subscription)
        self.AgencyUsersApi = AgencyUsersApi(subscription)


class AgencyAdministrationProduct(Product):

    def __init__(self, subscription):
        super().__init__('Agency Administration', '', subscription)
        self.AgencyStationsApi = AgencyStationsApi(subscription)


class AgencyClassesProduct(Product):
    def __init__(self, subscription):
        super().__init__('Agency Classes', '', subscription)
        self.AgencyClassesApi = AgencyClassesApi(subscription)
