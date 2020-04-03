# Subcriptions are for products, and products contain a number of seperate API's
from urllib.parse import urljoin
import requests
from .excpetion import WebCallException
from .util import BASE_URL


class API():

    def __init__(self, name, path, subscription):
        self.base = BASE_URL
        self.name = name
        self.path = path
        self.subscription = subscription

    def url(self):
        return urljoin(self.base, self.path)

    def make_call(self, path, params, retry=1):
        print(f'Making url call retry ={retry}')
        limit = 5
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription.Auth.primary_key,
            'Authorization': self.subscription.Auth.token.access_token
        }
        url = urljoin(self.url(), path)
        response = requests.get(url, params=params, headers=headers)
        if not response.ok and retry <= limit:
            if response.status_code == 401:
                self.subscription.Auth.get_token()
            retry += 1
            return self.make_call(path, params, retry)

        return response


class AgenyIncidentsApi(API):

    def __init__(self, subscription):
        super().__init__('Ageny Incidents', 'agencyincidents/', subscription=subscription)

    def get_incidents(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'incidents'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['incidents']
        else:
            raise WebCallException(response.status_code)

    def get_exposures(self, incidentID, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = f'incidents/{incidentID}/exposures'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['exposures']
        else:
            raise WebCallException(response.status_code)

    def get_all_exposures(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'incidents/exposures'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['exposures']
        else:
            raise WebCallException(response.status_code)

    def get_exposure_crew_members(self, exposureID, **kwargs):
        path = f'exposures/{exposureID}/crewmembers'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['crewMembers']
        else:
            raise WebCallException(response.status_code) 

    def get_all_exposure_crew_members(self, **kwargs):
        path = 'exposures/crewmembers'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['crewMembers']
        else:
            raise WebCallException(response.status_code)       

    def get_crew_memeber_roles(self, exposure_user_id, **kwargs):
        path = f'crewmembers/{exposure_user_id}/roles'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['roles']
        else:
            raise WebCallException(response.status_code)

    def get_exposure_location(self, exposureID, **kwargs):
        path = f'exposures/{exposureID}/location'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['exposureLocation']
        else:
            raise WebCallException

    def get_all_exposure_locations(self, **kwargs):
        path = 'exposures/location'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['exposureLocations']
        else:
            raise WebCallException

    def get_all_exposure_naratives(self, **kwargs):
        path = 'exposures/narratives'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['narratives']
        else:
            raise WebCallException


class AgencyUsersApi(API):

    def __init__(self, subscription):
        super().__init__('Ageny Users', 'agencyusers/', subscription)

    def get_users(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'users'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['users']
        else:
            raise WebCallException(response.status_code)


class AgencyStationsApi(API):

    def __init__(self, subscription):
        super().__init__('Ageny Stations', 'agencystations/', subscription)

    def get_stations(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'stations'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['stations']
        else:
            raise WebCallException(response.status_code)


class AgencyClassesApi(API):

    def __init__(self, subscription):
        super().__init__('Ageny Classes', 'agencyclasses/', subscription)

    def get_classes(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'classes'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['classes']
        else:
            raise WebCallException(response.status_code)

    def get_all_classes_students(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'classes/students'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['students']
        else:
            raise WebCallException(response.status_code)

    def get_all_classes_instructors(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'classes/instructors'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['instructors']
        else:
            raise WebCallException(response.status_code)

    def get_all_agency_code_categories(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'classes/agencycodecategories'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['agencyCodeCategories']
        else:
            raise WebCallException(response.status_code)

    def get_all_agency_codes(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'classes/agencycodes'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['agencyCodes']
        else:
            raise WebCallException(response.status_code)

    def get_all_classes_categories(self, **kwargs):
        '''
        kwargs are parsed as the get params. Valid args are:-
        rowVersion, limit, offset, filter, orderby
        '''
        path = 'classes/categories'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['categories']
        else:
            raise WebCallException(response.status_code)

    def get_class_category(self, categoryID, **kwargs):
        path = f'classes/categories/{categoryID}'
        response = self.make_call(path, kwargs)
        if response.ok:
            return response.json()['category']
        else:
            raise WebCallException