# Kloves

Do you want to...  
 * test how your app responds to a certain packet, specified down to its data fields?
 * test how your app responds to errant packets but have no way to trigger those actual errant packets?
 * test how your app handles rogue servers, which may just dump bytes/out-of-protocol packets, etc.?
 * play around with a synchronous protocol?

Then, this app might be the one you are looking for!

Do you want to...  
 * test connectivity issues (i.e., connection reliability, network latency)?
 * have an intelligent simulator which actually parses and processes packets for a given protocol?
 * play around with an asynchronous protocol?

This app is _not_ for you.

This is a general simulator app to test networking scenarios. Allows you to directly specify the packets
sent by some server (i.e., a "scripted" session). It is dumb, not intelligent, in the sense that it will
not send anything beyond the script given to it.

# Usage

**Important:** This script runs under Python 3.

    python3 kloves.py [hit type] [host] [port] [script file]

Where:
 * **hit type** is either `hit` or `wait`. A value of `hit` means that this instance of kloves will hit
   first the specified **host** and **port**. A value of `wait` means that this instance of kloves will
   wait for connections on the specified **host** and **port**; when a client connects in this mode,
   kloves will not do anything until the client hits with its own packet first.

   This means that you can have two instances of kloves running, one in `hit` mode, the other in `wait`,
   _talking to each other_.
  * **script file** is the order of packets which kloves will send out. See section below for the script
    file's specification.

## The script file

TODO since it is already 2:27 AM of the 9th of May 2013 and I am not on leave tomorrow.
