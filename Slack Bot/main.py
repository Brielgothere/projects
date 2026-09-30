import os
import time
from slackclient import SlackClient
from bot import parse_bot_commands


slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
starterbot_id = None
EXAMPLE_COMMAND = 'do'
RTM_READ_DELAY = 1

def handle_command(command, channel):
    default_response = f'Not sure what you mean. Try {EXAMPLE_COMMAND}'

    response = None

    if command.startswith(EXAMPLE_COMMAND):
        response = 'Sure....write some more code then I can do that!'


    slack_client.api_call(
        'chat.postMessage',
        channel=channel,
        text= response or default_response
    )





if __name__ == '__main__':
    if slack_client.rtm_connect(with_team_state= False):
        print('Starter Bot connected and running!')

        starterbot_id = slack_client.api_call('auth.test')['user_id']
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read(),starterbot_id)
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)

    else:
        print('Connection failed. Exception traceback printed above')