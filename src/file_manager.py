import base64
import os
from email.parser import BytesParser
from email.message import Message

class FileManager:

    def __init__(self, event):
        self.event = event
        self.boundary = event['headers']['Content-Type'].split("boundary=")[1]

    def save_file(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Base64 디코딩
        decoded_body = base64.b64decode(self.event['body'])
        
        # multipart/form-data 파싱을 위한 바운더리 설정
        headers = 'Content-Type: multipart/form-data; boundary=' + self.boundary
        msg = Message()
        msg.set_payload(decoded_body)
        msg.add_header('Content-Type', 'multipart/form-data', boundary=self.boundary)
        
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

        return filepath

        