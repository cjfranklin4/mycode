#!/usr/bin/env python
"""Alta3 Research | RZFeeser
   Any trace that is in *.pcapng must be first decoded to *.pcap
   this may be completed with the editcap utility. The editcap can be installed with tshark (sudo apt install tshark -y)

   editcap -F libpcap -T ether trace.pcapng trace.pcap
    
   The dpkt library is installed with:

   python3 -m pip install dpkt"""

# standard library
import datetime

# python3 -m pip install dpkt
import dpkt

# turn a hexadecimal address into a readable address
def mac_decode(old_mac):
    """returns a mac address decoded from hexadecimal
       this trick comes from the dpkt documentation"""
    return ':'.join('%02x' % dpkt.compat.compat_ord(b) for b in old_mac)

def main():

    # open the trace in read mode, and as a binary file
    # as long as we are indenting the file remains open
    with open('SIP_REGISTER_wp.pcap', 'rb') as f:

        # opens the file object with dpkt and exposes it to
        # the python sub-library "pypcap"
        pcap = dpkt.pcap.Reader(f)

        pkt_no = 0
        # ts is a timestamp, and buf is "buffered raw data"
        # this buffered raw data isn't too usable right away
        for ts, buf in pcap:

            pkt_no += 1
            print(f'Packet Number - {pkt_no}')

            # display teh timestamp in UTC format
            print(f'Timestamp: {datetime.datetime.utcfromtimestamp(ts)}')

            # unpack the ethernet frame (MAC source and destination)
            eth = dpkt.ethernet.Ethernet(buf) # here we tell dpkt that this is an Ethernet capture (layer 2)
            print(f'MAC source      - {mac_decode(eth.src)}')
            print(f'MAC Destination - {mac_decode(eth.dst)}')

if __name__ == "__main__":
    main()
