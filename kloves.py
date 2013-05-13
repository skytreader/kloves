#! /usr/bin/env python3

import socketserver
import sys

"""
The server backend to kloves.
"""

class KlovesServer(socketserver.ThreadingTCPServer):
    
    def __init__(self, server_address, handler_class, hit_mode):
        super(KlovesServer, self).__init__(server_address, handler_class)
        self.hit_mode = hit_mode

class KlovesHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        print("Created a server with hit mode " + self.server.hit_mode)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Improper usage!")
        exit()

    print("Waiting for connections...")
    # TODO Validate hit_mode
    server = KlovesServer(("localhost", 16981), KlovesHandler, sys.argv[1])
    server.serve_forever()
