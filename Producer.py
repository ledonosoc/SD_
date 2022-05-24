#!/usr/bin/env python
#
# Copyright 2020 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# =============================================================================
#
# Produce messages to Confluent Cloud
# Using Confluent Python Client for Apache Kafka
#
# =============================================================================

from urllib.parse import uses_params
from confluent_kafka import Producer, KafkaError
import json
import ccloud_lib
import time


def Producer(User):

    # Read arguments and configurations and initialize
    config_file = open('librdkafka.config','r')
    topic = "Usuarios"
    conf = ccloud_lib.read_ccloud_config(config_file)

    # Create Producer instance
    producer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)
    producer = Producer(producer_conf)

    # Create topic if needed
    ccloud_lib.create_topic(conf, topic)

    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Error al ingresar usuario: {}".format(err))
        else:
            print("Usuario [{}] tiempo de acceso {} ingresado correctamente"
                  .format(msg.partition(), msg.offset()))

    record_key = User
    record_value = json.dumps({'time': time.time()})
    print("Ingresando al usuario: {}\t{}".format(record_key, record_value))
    producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)
    # p.poll() serves delivery reports (on_delivery)
    # from previous produce() calls.
    producer.poll(0)

    producer.flush()
