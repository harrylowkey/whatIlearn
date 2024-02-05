FROM public.ecr.aws/docker/library/node:20-slim AS development
WORKDIR /usr/src/app
ARG ENVIRONMENT
RUN npm install -g pnpm@8.14.1
RUN apt-get update -y && \
    apt-get install -y libtool automake autoconf nasm
COPY package.json pnpm-lock.yaml ./
COPY environments/${ENVIRONMENT}.env .env
RUN pnpm install
ADD . .
RUN pnpm start

FROM public.ecr.aws/nginx/nginx as production
ADD nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=development /usr/src/app/public /usr/share/nginx/html
EXPOSE 2000
# it is nginx port that has been defined in nginx.conf file

