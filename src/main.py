import json
import logging
import json

logger = logging.getLogger()

def main(event, context):
    print(event)
    logger.info(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
