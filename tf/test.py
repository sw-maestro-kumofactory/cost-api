import base64
import os
from email.parser import BytesParser
from email.message import Message

def save_body_to_file(event_body, directory, boundary):

    if not os.path.exists(directory):
        os.makedirs(directory)

    # Base64 디코딩
    decoded_body = base64.b64decode(event_body)
    
    # multipart/form-data 파싱을 위한 바운더리 설정
    headers = 'Content-Type: multipart/form-data; boundary=' + boundary
    msg = Message()
    msg.set_payload(decoded_body)
    msg.add_header('Content-Type', 'multipart/form-data', boundary=boundary)
    
    # 바이트 파서를 사용하여 메시지 파싱
    parser = BytesParser()
    parsed_msg = parser.parsebytes(headers.encode() + b"\n\n" + decoded_body)

    for part in parsed_msg.walk():
        # 파일 이름 추출
        content_disposition = part.get('Content-Disposition')
        if content_disposition and 'filename' in content_disposition:
            filename = content_disposition.split('filename=')[1].strip('"')
            filepath = os.path.join(directory, filename)
            
            # 파일 저장
            with open(filepath, 'wb') as file:
                file.write(part.get_payload(decode=True))
            print(f"Saved to {filepath}")


event = {'resource': '/infracost-lambda', 'path': '/infracost-lambda', 'httpMethod': 'POST', 'headers': {'accept': '*/*', 'content-type': 'multipart/form-data; boundary=------------------------3a7d3b584a14b3d9', 'Host': 'oeejfb9dqe.execute-api.ap-northeast-2.amazonaws.com', 'User-Agent': 'curl/7.81.0', 'X-Amzn-Trace-Id': 'Root=1-65106e4f-54392c537ba0f58a39b0efe3', 'x-api-key': 'LTzz04tGiJ9Z3us7x4rqj9NIK7AGuCAS7VVUjs62', 'X-Forwarded-For': '15.165.11.115', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'accept': ['*/*'], 'content-type': ['multipart/form-data; boundary=------------------------3a7d3b584a14b3d9'], 'Host': ['oeejfb9dqe.execute-api.ap-northeast-2.amazonaws.com'], 'User-Agent': ['curl/7.81.0'], 'X-Amzn-Trace-Id': ['Root=1-65106e4f-54392c537ba0f58a39b0efe3'], 'x-api-key': ['LTzz04tGiJ9Z3us7x4rqj9NIK7AGuCAS7VVUjs62'], 'X-Forwarded-For': ['15.165.11.115'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'nom37z', 'resourcePath': '/infracost-lambda', 'httpMethod': 'POST', 'extendedRequestId': 'LxYsgGH1oE0FhFg=', 'requestTime': '24/Sep/2023:17:13:51 +0000', 'path': '/default/infracost-lambda', 'accountId': '434126037102', 'protocol': 'HTTP/1.1', 'stage': 'default', 'domainPrefix': 'oeejfb9dqe', 'requestTimeEpoch': 1695575631732, 'requestId': 'f0e18917-eedb-4b3e-bb0b-ec055e15e225', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None, 'apiKey': 'LTzz04tGiJ9Z3us7x4rqj9NIK7AGuCAS7VVUjs62', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': None, 'apiKeyId': 'qqm2qrcrpl', 'userAgent': 'curl/7.81.0', 'accountId': None, 'caller': None, 'sourceIp': '15.165.11.115', 'accessKey': None, 'cognitoAuthenticationProvider': None, 'user': None}, 'domainName': 'oeejfb9dqe.execute-api.ap-northeast-2.amazonaws.com', 'apiId': 'oeejfb9dqe'}, 'body': 'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0zYTdkM2I1ODRhMTRiM2Q5DQpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9ImZpbGUiOyBmaWxlbmFtZT0ibWFpbi50ZiINCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtDQoNCnByb3ZpZGVyICJhd3MiIHsKICByZWdpb24gICAgICAgICAgICAgICAgICAgICAgPSAidXMtZWFzdC0xIgogIHNraXBfY3JlZGVudGlhbHNfdmFsaWRhdGlvbiA9IHRydWUKICBza2lwX3JlcXVlc3RpbmdfYWNjb3VudF9pZCAgPSB0cnVlCiAgYWNjZXNzX2tleSAgICAgICAgICAgICAgICAgID0gIm1vY2tfYWNjZXNzX2tleSIKICBzZWNyZXRfa2V5ICAgICAgICAgICAgICAgICAgPSAibW9ja19zZWNyZXRfa2V5Igp9CgpyZXNvdXJjZSAiYXdzX2luc3RhbmNlIiAid2ViX2FwcCIgewogIGFtaSAgICAgICAgICAgPSAiYW1pLTY3NGNiYzFlIgogIGluc3RhbmNlX3R5cGUgPSAibTUuNHhsYXJnZSIgICAgICAgICAgICAgICMgPDw8PDwgVHJ5IGNoYW5naW5nIHRoaXMgdG8gbTUuOHhsYXJnZSB0byBjb21wYXJlIHRoZSBjb3N0cwoKICByb290X2Jsb2NrX2RldmljZSB7CiAgICB2b2x1bWVfc2l6ZSA9IDUwCiAgfQoKICBlYnNfYmxvY2tfZGV2aWNlIHsKICAgIGRldmljZV9uYW1lID0gIm15X2RhdGEiCiAgICB2b2x1bWVfdHlwZSA9ICJpbzEiICAgICAgICAgICAgICAgICAgICAgIyA8PDw8PCBUcnkgY2hhbmdpbmcgdGhpcyB0byBncDIgdG8gY29tcGFyZSBjb3N0cwogICAgdm9sdW1lX3NpemUgPSA1MDAKICAgIGlvcHMgICAgICAgID0gODAwCiAgfQp9CgpyZXNvdXJjZSAiYXdzX2xhbWJkYV9mdW5jdGlvbiIgImhlbGxvX3dvcmxkIiB7CiAgZnVuY3Rpb25fbmFtZSA9ICJoZWxsb193b3JsZCIKICByb2xlICAgICAgICAgID0gImFybjphd3M6bGFtYmRhOnVzLWVhc3QtMTphY2NvdW50LWlkOnJlc291cmNlLWlkIgogIGhhbmRsZXIgICAgICAgPSAiZXhwb3J0cy50ZXN0IgogIHJ1bnRpbWUgICAgICAgPSAibm9kZWpzMTIueCIKICBtZW1vcnlfc2l6ZSAgID0gMTAyNCAgICAgICAgICAgICAgICAgICAgICAjIDw8PDw8IFRyeSBjaGFuZ2luZyB0aGlzIHRvIDUxMiB0byBjb21wYXJlIGNvc3RzCn0NCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tM2E3ZDNiNTg0YTE0YjNkOS0tDQo=', 'isBase64Encoded': True}
# boundary 정보 추출
boundary = event['headers']['content-type'].split("boundary=")[1]

# 사용 예시:
save_body_to_file(event['body'], './test', boundary)
print("Done")
