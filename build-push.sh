#!/bin/bash

PARAMETER=$1

# 매개변수가 비어 있는지 확인
if [ -z "$PARAMETER" ]; then
    echo "매개변수"
    exit 1
fi

docker build -t 434126037102.dkr.ecr.ap-northeast-2.amazonaws.com/infracost-lambda:$PARAMETER .
docker push 434126037102.dkr.ecr.ap-northeast-2.amazonaws.com/infracost-lambda:$PARAMETER