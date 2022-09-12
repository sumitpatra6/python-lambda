import json
import logging
import json

logger = logging.getLogger()

def main(event, context):
    print(event)
    operation = event.get("httpMethod", "")
    payload = event.get("body", {})
    logger.info(event)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'event' : event
        })
        
    }
