import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

# Data is published along with a topic. The subscribers usually sets a filter on these topics
# for topic of their interests
message_count = 1
while True:
    # topic = random.randrange(9999, 10005)
    # messagedata = random.randrange(1, 215) - 80
    # print "%d %d" % (topic, messagedata)

    socket.send("{} {} x Some Message".format("topic", message_count))
    print "Sending {}".format(message_count)
    # message_count += 1
    time.sleep(1)