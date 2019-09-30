from kafka import KafkaConsumer


def show(args):
    print args


class Worker:
    def __init__(self, **kwargs):
        topic = kwargs.get('topic','test')
        bootstrap_servers = [kwargs['url']]
        client_id = kwargs.get('client_id')
        if client_id:
            self.client = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, client_id=client)
        else:
            self.client = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest', enable_auto_commit=False)
        self.jobs = iter(self.client)

    def compute(self, f):
        f(self.jobs.next())


