FROM node:16.13.0-bullseye as build-stage

ENV REACT_APP_ENVIRONMENT=staging

WORKDIR /app
COPY . .
RUN yarn install --frozen-lockfile && yarn build


FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
