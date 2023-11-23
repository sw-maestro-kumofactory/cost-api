#!/bin/bash

PARAMETER=$1

# 매개변수가 비어 있는지 확인
if [ -z "$PARAMETER" ]; then
    echo "매개변수"
    exit 1
fi

# Docker 컨테이너 실행 명령어
docker run -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 \
    --entrypoint /aws-lambda/aws-lambda-rie \
    434126037102.dkr.ecr.ap-northeast-2.amazonaws.com/infracost-lambda:$PARAMETER \
    /usr/local/bin/python -m awslambdaric lambda_function.handler
