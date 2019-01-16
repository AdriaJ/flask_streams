How to use these codes ?

Install Zookeeper and Kafka, using for example this site :
https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm

Keep he servers running, or start them again with commands shown on this page :
https://www.tutorialspoint.com/apache_kafka/apache_kafka_basic_operations.htm
i.e. (in your kafka directory):
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

You should verify everything is running well with command
jps
You should see Jps, Kafka and QuorumPeerMain precesses.


Go to this git directory and activate virtual environment with 
source env/bin/activate

Then you can start your kafka work, either with a stream of images or a stream of text.
In a terminal, run a producer, and in another one run the consumer.

text_producer.py works with consumer.py
producer.py works with video_consumer.py


Don't forget to link the emitting port of Flask inyour virtual machine (usually localhost:5000) to
a free port on your local machine with the parameter -L set to <your_port_number>:localhost:5000
in your SSH connecion command to the VM to see the display locally.
