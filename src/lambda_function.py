import sys
import subprocess
import json
import base64
import uuid

import logging

import os

from file_manager import FileManager
from cf2tf.app import convert_and_save

from hotfix import func

log = logging.getLogger("cf2tf")


def handler(event, context):
    folder_name = str(uuid.uuid4())

    print(event)

    # 파일 저장
    file_manager = FileManager(event)
    filepath = file_manager.save_file('/tmp/'+folder_name)

    # 파일 수정
    func(filepath)
    with open(filepath, 'r') as file:
        updated_data = json.load(file)
        print("Updated file content:")
        print(updated_data)
    
    # 파일 변환
    convert_and_save(filepath, '/tmp/'+folder_name)

    # file read and print to console (/tmp/folder_name/resource.tf)
    with open('/tmp/'+folder_name+'/resource.tf', 'r') as file:
        print("Terraform file content:")
        print(file.read())

    cmd = "infracost breakdown --path /tmp/"+folder_name+" --format json"

    raw_output = run_command(cmd)
    output = json.loads(raw_output)

    print(raw_output)


    response = {
        "statusCode": 200,
        "headers": {
            "x-custom-header" : "우리 그만하자 람다야"
        },
        "body": json.dumps(output)

    }

    return response


def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout