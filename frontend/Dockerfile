# build environment
FROM node:latest as build-deps
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn --silent
COPY . /app
RUN yarn build:staging

# production environment
FROM nginx:1.12-alpine
COPY --from=build-deps /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]