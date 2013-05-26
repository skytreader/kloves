#! /usr/bin/env python3

from script_parser import TextScriptParser

import socketserver
import sys

"""
The server backend to kloves.
"""

class KlovesServer(socketserver.ThreadingTCPServer):
    
    def __init__(self, server_address, handler_class, hit_mode, packet_list, delimiters):
        """
        server_address - iterable containing the host and port, in that order
        handler_class - the class name of the handler for this server
        hit_mode - the mode of this server (either "hit" or "wait")
        packet_list - the list of packet strings to be sent by this server
        delimiters - iterable containing the start delimiter of a packet
            and the end delimiter of a packet, in that order.
        """
        super(KlovesServer, self).__init__(server_address, handler_class)
        self.hit_mode = hit_mode
        self.packet_list = packet_list
        self.delimiters = delimiters

class KlovesHandler(socketserver.BaseRequestHandler):
    
    # TODO Make this an attribute of KlovesHandler
    BUFFER_SIZE = 1024

    def get_packet(self):
        """
        Receives requests, starting with the start delimiter for a packet,
        until it encounters the end delimiter for the packet.
        """
        whole_packet = ""

    def handle(self):
        if self.server.hit_mode == "wait":
            # block here
            print("My hit mode is wait")
            pass

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 " + sys.argv[0] + " [hit type] [host] [port] [script file]")
        exit()
    
    hit_mode = sys.argv[1].lower()

    if hit_mode not in ("hit", "wait"):
        print("Valid [hit type] values are either `hit` or `wait`")
        exit()

    host = sys.argv[2]
    port = int(sys.argv[3])
    print("Started with hit type `" + hit_mode + "`")
    script_file = sys.argv[4]
    print("Waiting for connections at " + host + ":" + sys.argv[3])
    server = KlovesServer((host, port), KlovesHandler, hit_mode, [], ())
    server.serve_forever()
