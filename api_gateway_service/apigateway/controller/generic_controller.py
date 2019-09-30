import json
from apigateway.conf.resource import GenericResource
from flask import request
import requests
from apigateway.utils.config_utils import get_env_config
from apigateway.core.header_context import get_header_dict


config = get_env_config()


def get_mapped_route(resource_name):
    routes = {
        "endpoint": config.USER_SERVICE_URL+"/endpoint/{}",
        "ping":config.QA_SERVICE_URL+"/questionanswer/ping",
        "topic": config.QA_SERVICE_URL + "/questionanswer/topic",
        "subtopic": config.QA_SERVICE_URL + "/questionanswer/subtopic",
        "question": config.QA_SERVICE_URL + "/questionanswer/question",
        "testcase": config.QA_SERVICE_URL + "/questionanswer/testcase"
    }
    print "***************** in dict***********************"
    return routes[resource_name]


class GenericHandler(GenericResource):
    def get(self, resource_name, resource_id=None):
        url_path = get_mapped_route(resource_name)
        url = url_path.format(resource_id + "/" if resource_id else "")

        param = dict(request.args)
        param_list = []
        for k in param:
            for i in param[k]:
                param_list.append(str(k) + '=' + str(i))
        string = '&'.join(param_list)
        string = '?' + string if string else string
        url = url + string if string else url
        response = requests.get(url,
                                headers=get_header_dict(request.headers))
        status_code = response.status_code

        return response.json(), status_code, {}


    def put(self, resource_name, resource_id=None):
        url_path = get_mapped_route(resource_name)
        url = url_path.format(resource_id + "/" if resource_id else "")

        data = request.get_json(force=True)

        response = requests.put(url,
                                headers=get_header_dict(request.headers),
                                params=request.args.to_dict(),
                                data=json.dumps(data))
        status_code = response.status_code
        return response.json(), status_code, {}

    def post(self, resource_name, resource_id=None):
        url_path = get_mapped_route(resource_name)
        url = url_path.format(resource_id if resource_id else "")
        data = request.get_json(force=True)
        response = requests.post(url,
                                 headers=get_header_dict(request.headers),
                                 data=json.dumps(data))
        status_code = response.status_code
        return response.json(), status_code, {}

    def patch(self, resource_name, resource_id=None):
        url_path = get_mapped_route(resource_name)
        url = url_path.format(resource_id if resource_id else "")
        data = request.get_json()
        response = requests.patch(url,
                                  headers=get_header_dict(request.headers),
                                  data=json.dumps(data))
        status_code = response.status_code
        return response.json(), status_code, {}

