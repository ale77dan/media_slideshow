#!/usr/bin/env python
import socket, time, string, os

# Open a UDP socket...
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ...and "connect" it to the address of info-beamer
sock.connect(('127.0.0.1', 4444))

script_dir = os.path.dirname(__file__)
num = 1;
while True:
    # The name of the current directory is 'synchronized', the name of the first
    # child directory is 'child1'. Therefore the complete path to address the
    # first child is 'synchronized/child1'. You can also see this path in the
    # console output of the running info-beamer. Look for "Hello from node child1"
    # and look at its prefix.

    # The 'set_text' is a path component that is then provided to the 'child1' node 
    # and can be used to have multiple functions listening using data_mapper. 
    # Currently only 'set_text' is defined.

    # Everything after the ':' is given as an argument to the function defined in
    # data_mapper. We use it to update a variable that is displayed on screen.
    sock.send('default_nodes/template:default')
    time.sleep(10)

    rel_path = "child3/playlist.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    out_file = open(abs_file_path,"w")
    out_file.write(str(num)  + ".mp4\n")
    out_file.close()
    sock.send('default_nodes/template:fullscreen')
    time.sleep(10)

    num = num +1;