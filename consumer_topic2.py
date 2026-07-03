from kafka import KafkaConsumer
from const import *
import sys
import json

try:
    topic = sys.argv[1]
except:
    topic = TOPIC_2

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
    auto_offset_reset='earliest',
    group_id='final-consumer',
    value_deserializer=lambda value: json.loads(value.decode())
)

print('Consuming processed events from ' + topic)

for msg in consumer:
    print('Final event: ' + str(msg.value))
