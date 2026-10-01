import re
from slackclient import SlackClient


def parse_direct_mention(message_text):
    MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
    matches = re.search(MENTION_REGEX, message_text)
    return (matches.group(1), matches.group(2).strip() if matches else (None,None))

def  parse_bot_commands(slack_events, starterbot_id):
    for event in slack_events:
        if event['type'] == 'message' and not 'subtype' in event:
            user_id, message = parse_direct_mention(event['text'])

            if user_id == starterbot_id:
                return message, event['channel']

    return None, None


