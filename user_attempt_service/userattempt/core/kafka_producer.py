from kafka import KafkaProducer


class MessageQueue:
    def __init__(self, **kwargs):
        url = kwargs.get('url', 'localhost:9092')
        self.client = KafkaProducer(bootstrap_servers=url, api_version=(0,10))

    def queue(self, topic='test', key=None, msg=None):
        if not msg:
            raise Exception
        self.client.send(topic, key=key, value=msg)

    def flush(self):
        self.client.flush()

if __name__ == '__main__':
    queue = MessageQueue(url='13.228.224.134:9092')
    for i in range(10):
        queue.queue(topic='test1', msg='Hello World{}'.format(i), key=str(i%4))
