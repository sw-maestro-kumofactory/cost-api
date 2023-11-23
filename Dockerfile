ARG FUNCTION_DIR="/function"

FROM python:3.11-alpine3.16 as build-image

RUN apk add --no-cache \
    build-base \
    git \
    libtool \ 
    autoconf \ 
    automake \ 
    libexecinfo-dev \ 
    make \
    cmake \ 
    libcurl 

RUN git clone --depth 1 https://github.com/hashicorp/terraform-provider-aws.git /tmp/terraform_src

ARG FUNCTION_DIR
RUN mkdir -p ${FUNCTION_DIR}

RUN python -m pip install --upgrade pip
RUN python -m pip install \
        --target ${FUNCTION_DIR} \
        awslambdaric \
        boto3 \ 
        requests

RUN python -m pip install \
        --target ${FUNCTION_DIR} \
        cfn-flip \
        PyYAML \
        GitPython \
        thefuzz[speedup] \
        pytest

FROM python:3.11-alpine3.16

RUN apk add --no-cache \
    libstdc++ \
    git \
    curl && \
    rm -rf /var/cache/apk/* && \
    curl -fsSL https://raw.githubusercontent.com/infracost/infracost/master/scripts/install.sh | sh && \
    infracost configure set api_key [api token]

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}
# COPY --from=build-image /tmp/terraform_src/website/docs ${FUNCTION_DIR}/website/docs

COPY src/ ${FUNCTION_DIR}
COPY cf2tf/ ${FUNCTION_DIR}/cf2tf

RUN git clone --depth 1 https://github.com/sw-maestro-kumofactory/terraform-provider-aws.git /function/terraform_src && \
    ls /function/terraform_src 

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "lambda_function.handler" ]