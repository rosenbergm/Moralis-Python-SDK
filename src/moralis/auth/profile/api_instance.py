import openapi_auth
from openapi_auth.apis.tags import profile_api
from ..utilities import get_common_headers


def get_api_instance(api_key):
    configuration = openapi_auth.Configuration()
    configuration.api_key['ApiKeyAuth'] = api_key
    api_client = openapi_auth.ApiClient(configuration)
    headers = get_common_headers()
    for header in headers:
        api_client.default_headers[header] = headers[header]
    api_instance = profile_api.ProfileApi(api_client)
    api_client.close()

    return api_instance
