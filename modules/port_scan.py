#/usr/bin/python

import socket
import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip", dest="ip", help="Sepcify target ip or ip range")
    options = parser.parse_args()
    return  options


options = get_arguments()
result_list = scan(options.target)
print_result(result_list)
