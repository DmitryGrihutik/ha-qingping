from .utils import parser

def decode(topic, payload):

    try:
        addr = topic.value.split('/')[1]
        data = parser.parse_data(payload)

        r = {
            "addr": addr,
            "data": data,
        }

        return r
    except:
        return False