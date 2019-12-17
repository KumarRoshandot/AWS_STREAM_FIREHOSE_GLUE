from __future__ import print_function

import base64
import json

print('Loading function')


def lambda_handler(event, context):
    output = []
    succeeded_record_cnt = 0
    failed_record_cnt = 0

    for record in event['records']:
        payload = base64.b64decode(record['data'])
        data = base64.b64encode(json.dumps(data_field))
	output.append(data)
    return {output}
