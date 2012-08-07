class PubHandler(Object):

    def __init__(self):
        self.topics = {}

    def list_publishers(topic):
        return self.topics[topic]

    def add_publisher_to_topics(pub_id, topics=[]):
        for topic in topics:
            if not self.topics.has_key(topic):
                self.topics[topic] = []
            self.topics[topic].append(pub_id)

    def del_publisher_from_topics(pub_id, topics=[]):
        for topic in topics:
            if self.topics.has_key(topic):
                self.topics[topic].remove(pub_id)

