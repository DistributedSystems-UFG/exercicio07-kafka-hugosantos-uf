from kafka import KafkaProducer
from const import *
import sys
import json
from datetime import datetime, timezone

try:
    topic = sys.argv[1]
except:
    topic = TOPIC_1
    
producer = KafkaProducer(
    bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
    value_serializer=lambda value: json.dumps(value).encode()
)

for i in range(100):
    event = {
        'id': i,
        'type': 'raw_event',
        'value': i,
        'created_at': datetime.now(timezone.utc).isoformat()
    }
    print('Sending event: ' + str(event))
    producer.send(topic, value=event)

producer.flush()
