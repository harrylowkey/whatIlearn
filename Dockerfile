FROM public.ecr.aws/docker/library/python:3.11.6-alpine as builder
RUN apk update
WORKDIR /usr/app
COPY portfolio/requirements.txt .
RUN pip install -r requirements.txt


FROM public.ecr.aws/docker/library/python:3.11.6-alpine as production
RUN apk update && apk add bash
WORKDIR /usr/app
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/include /usr/local/include
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
RUN chmod +x ./portfolio/startup.sh
EXPOSE 3000
CMD ["/bin/bash","-c","./portfolio/startup.sh"]
