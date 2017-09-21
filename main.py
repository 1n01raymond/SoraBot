import time
import  random
from slackclient import SlackClient

SLACK_BOT_TOKEN = 'xoxb-244461179202-4JMGwXTUHv87QyocC6D2yQLt'
BOT_NAME = 'sora'
SORA = '소라고둥님'
SORA_ANSWER = ['응', '아니야', '응 아니야', '그래', '카레', '하지마', '해', '고양이 조아']
READ_DELAY = 1

slack_client = SlackClient(SLACK_BOT_TOKEN)


def parse(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and SORA in output['text']:
                return True, output['channel']

    return False, None


def handle(channel):
    answer = SORA_ANSWER[random.randrange(0, len(SORA_ANSWER))]
    slack_client.api_call("chat.postMessage", channel=channel, text=answer, as_user=True)


if __name__ == "__main__":
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            has_sora, channel = parse(slack_client.rtm_read())
            if has_sora:
                handle(channel)

            time.sleep(READ_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
