import re
from slackclient import SlackClient



EXAMPLE_COMMAND = 'do'
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)

    

def  parse_bot_commands(slack_events, starterbot_id):
    for event in slack_events:
        if event['type'] == 'message' and not 'subtype' in event:
            user_id, message = parse_direct_mention(event['text'])

            if user_id == starterbot_id:
                return message, event['channel']

    return None, None


