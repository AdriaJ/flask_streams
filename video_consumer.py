from flask import Flask, Response
from kafka import KafkaConsumer
#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('video-topic', group_id='view', bootstrap_servers=['0.0.0.0:9092'])
#Continuously listen to the connection and print messages as recieved
app = Flask(__name__)

@app.route('/')
def index():
    return('Flask application running on ec2...')


@app.route('/stream')
def stream():
    # return a multipart response
#    return Response(text_stream())
    return(Response(kafkastream(), mimetype='multipart/x-mixed-replace; boundary=frame'))
#	mimetype='text/plain')
#                    mimetype='multipart/x-mixed-replace; boundary=frame')
#    return 'working ...'

def text_stream():
    for msg in consumer:
#        print(msg.value.decode('utf-8'))
        yield(msg.value.decode('utf-8'))
        yield('\n')

def kafkastream():
    for msg in consumer:
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + msg.value + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
#    text_stream()
