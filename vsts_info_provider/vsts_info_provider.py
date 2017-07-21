# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from __future__ import print_function
from sys import stderr
from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from . import models
from .version import VERSION


class VstsInfoProviderConfiguration(Configuration):
    """Configuration for VstsInfoProvider
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param api_version: Version of the API to use.  This should be set to
     '3.2-preview' to use this version of the api.
    :type api_version: str
    :param str base_url: Service URL
    """

    def __init__(
            self, api_version, base_url=None):

        if api_version is None:
            raise ValueError("Parameter 'api_version' must not be None.")
        if not isinstance(api_version, str):
            raise TypeError("Parameter 'api_version' must be str.")
        if not base_url:
            base_url = 'https://{}.visualstudio.com/'

        super(VstsInfoProviderConfiguration, self).__init__(base_url)

        self.add_user_agent('azurecli/{} vstsinfo/{}'.format(VERSION, VERSION))

        self.api_version = api_version


class VstsInfoProvider(object):
    """VstsInfoProvider

    :ivar config: Configuration for client.
    :vartype config: AzureTfsConfiguration

    :param api_version: Version of the API to use.  This should be set to
     '3.2-preview' to use this version of the api.
    :type api_version: str
    :param str vsts_git_url: vsts git URL
    :param Credentials creds: credentials for vsts
    """

    def __init__(
            self, api_version, vsts_git_url, creds=None):
        self.config = VstsInfoProviderConfiguration(api_version, vsts_git_url)
        self._client = ServiceClient(creds, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '3.2' if not api_version else api_version
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    def get_vsts_info(
            self, custom_headers=None, raw=False, **operation_config):
        """GetContinuousDeploymentOperation.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`ContinuousDeploymentOperation
         <vsts_info_provider.models.ContinuousDeploymentOperation>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = '/vsts/info'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)
        if response.status_code not in [200]:
            print("response:", response.status_code, file=stderr)
            print(response.text, file=stderr)
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VstsInfo', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
