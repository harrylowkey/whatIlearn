FROM node:18-alpine As development
RUN apk update && apk add --no-cache bash git openssh
WORKDIR /usr/src/app
ADD package*.json ./
ADD .npmrc ./
RUN npm install
ADD . .
RUN npm run build

FROM node:18-alpine as production
WORKDIR /usr/src/app
ADD package*.json ./
COPY --from=0 /usr/src/app/node_modules/ ./node_modules/
RUN npm install
COPY --from=development /usr/src/app/dist ./dist
EXPOSE 3000
CMD ["node", "/usr/src/app/dist/main.js"]
