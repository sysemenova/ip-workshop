## ip-workshop
This is a repository for the code used and shown during the Intro to Networking workshop for Open Sourcery at UMD.

## Demo 1
This demos sends an ICMP packet to whichever website and has you watch the machines the packet hits!

On windows, `tracert <website name>`, for example `tracert google.com`
On mac and linux, `traceroute <website name>`.

If you want to learn a bit more about traceroute (and tracert, which is basically the same thing), [here's a website for that]{https://www.redhat.com/sysadmin/traceroute-finding-meaning}.

## Demo 2

This demo sends a UDP packet from one python script to another one. More details on running it and the code itself is in the folder `demo2`.

### Demo 2.5

Here, I show NAT happening! The configuration I'm running the scripts on is the following: there are two machines on campus that I'm connecting to. Both of them are within the same general private network (the way we all are), but with a layer of NAT separating them. The exact architecture isn't known, but it's clear to see *some* NAT is happening, since the IP is changing!
