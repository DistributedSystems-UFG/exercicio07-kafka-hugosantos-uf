[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AyCg-K9D)
# pub-sub-basics-with-kafka
Very simple pub-sub example

## Follow these steps to run a Kafka broker on a server (with at least 2GB of RAM, such as AWS instance type t3-small):

- Open a command-line interface (shell) on the server

### Install and configure Apache Kafka (this is necessary only when running Kafka for the first time on the machine):

#### Install Java (JDK)
```
sudo apt update
```
```
sudo apt install default-jdk
```
#### Download, install (just uncompress) and configure Apache Kafka. For more detailed instructions, see Kafka's Quickstart page: https://kafka.apache.org/quickstart
  
```
wget https://dlcdn.apache.org/kafka/4.2.0/kafka_2.13-4.2.0.tgz
```
```
tar -xzf kafka_2.13-4.2.0.tgz
```

#### Basic configuration of Kafka (for remote access to the broker)
```
cd kafka_2.13-4.2.0/
```

**Enable remote access to the broker:** Edit the file **config/server.properties** (in the kafka directory) in order to change the line starting with **advertised_listeners**, replacing (only) the first occurrence of **localhost** with the **IP address** of the machine where the Broker will run (server01). It is recommended to use a fixed public IP address for this machine. That line should look like this:

advertised.listeners=PLAINTEXT://32.195.37.234:9092,CONTROLLER://localhost:9093

#### Then create the metadata files with the configuration
```
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```
```
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
```

#### Once configured, run the following command to start the broker
```
bin/kafka-server-start.sh config/server.properties
```

## For the clients:

### Install the Kafka Python client

```
sudo apt update
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install kafka-python
```

### Run the final consumer for topic2
```
python3 consumer_topic2.py topic2
```

### Run the processing consumer for topic1 and producer for topic2
```
python3 consumer.py topic1 topic2
```

### Run the producer for topic1
```
python3 producer.py topic1
```

This implements the requested flow:

```
producer(topic1) --> consumer(topic1)/producer(topic2) --> consumer(topic2)
```
