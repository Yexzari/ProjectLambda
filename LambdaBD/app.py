import json
from common.utils import get_db_connection

def lambda_handler(event,__):
    group = event['group']
    grade = event['grade']

    connection = get
