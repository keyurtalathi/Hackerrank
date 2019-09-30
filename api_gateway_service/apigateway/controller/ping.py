from apigateway.conf.resource import BaseResource


class Ping(BaseResource):
    def get(self):
        return {"response": "All OK"}

    # get.authenticated = False