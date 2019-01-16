# producer.py

import time
import cv2
from kafka import SimpleProducer, KafkaClient
#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
# Assign a topic
topic = 'my-topic'

def text_emitter(text):
    file = open(text, 'rb')
    print("emitting...")
    
    #reading file
    for line in file:
        producer.send_messages(topic, line)
        time.sleep(.1)
    
    file.close()
    print("done emitting")

if __name__ == '__main__':
    text_emitter('thereseRaquin.txt')
