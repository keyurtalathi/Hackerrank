from examination.conf.resource import BaseResource


class Ping(BaseResource):
    def get(self):
        return {"response": "All OK"}
