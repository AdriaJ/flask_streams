from flask import Flask, Response
from kafka import KafkaConsumer
#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('my-topic', group_id='view', bootstrap_servers=['0.0.0.0:9092'])
#Continuously listen to the connection and print messages as recieved
app = Flask(__name__)

@app.route('/')
def index():
    return('Flask application running on ec2...')


@app.route('/stream')
def stream():
    return Response(text_stream())
#    return(Response(kafkastream(), mimetype='multipart/x-mixed-replace; boundary=frame'))
#	mimetype='text/plain')
#                    mimetype='multipart/x-mixed-replace; boundary=frame')

def text_stream():
    for msg in consumer:
        yield(msg.value.decode('utf-8'))
        yield('\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
