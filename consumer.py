from kafka import KafkaConsumer, KafkaProducer
from const import *
import sys
import json
from datetime import datetime, timezone

try:
    input_topic = sys.argv[1]
except:
    input_topic = TOPIC_1

try:
    output_topic = sys.argv[2]
except:
    output_topic = TOPIC_2

consumer = KafkaConsumer(
    input_topic,
    bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
    auto_offset_reset='earliest',
    group_id='event-processor',
    value_deserializer=lambda value: json.loads(value.decode())
)

producer = KafkaProducer(
    bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
    value_serializer=lambda value: json.dumps(value).encode()
)

print('Processing events from ' + input_topic + ' and publishing to ' + output_topic)

for msg in consumer:
    event = msg.value
    processed_event = {
        'id': event['id'],
        'type': 'processed_event',
        'original_value': event['value'],
        'processed_value': event['value'] * 2,
        'source_topic': msg.topic,
        'processed_at': datetime.now(timezone.utc).isoformat()
    }

    print('Processed event: ' + str(processed_event))
    producer.send(output_topic, value=processed_event)
    producer.flush()
