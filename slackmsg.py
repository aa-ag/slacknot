# 2 functions needed:
# main(): driver, which accepts input messages via CLI
# post(): sends inputed message to slack using requests + SLACK API

#--- imports ---#
import requests
import sys
import getopt # "This module helps scripts to parse the command line arguments in sys.argv. " 
# https://docs.python.org/3/library/getopt.html
import config

#--- functions ---#

def send_message_to_slack(message_for_slack):
    # send json formatted string to payload
    payload = '{"text":"%s"}' % message_for_slack

    # post payload to API endpoint
    response = requests.post(f'{config.API_KEY}', data=payload)

    #should get 200 status code
    print(response.text)


def main(argv):
    message_for_slack = '' # placeholder for input

    try:
        opts, args = getopt.getopt(argv, 'hm:', ["message_for_slack="])
    except getopt.GetoptError:
        print("slackmsg.py -m <message_for_slack>")
        sys.exit(2)

    if len(opts) == 0:
        message_for_slack = 'This is a default message.'

    for opt, arg in opts:
        if opt == "-h":
            print("slackmsg.py -m <message_for_slack>")
            sys.exit()
        elif opt in ("-m", "--message"):
            message_for_slack = arg

    send_message_to_slack(message_for_slack)

if __name__ == "__main__":
    main(sys.argv[1:])
