import { isDevelopment } from "./helper/is-development";

export const config = {
  webSocketPort: 7700,
  baseUri: isDevelopment
    ? `${window.location.protocol}//${window.location.hostname}:7701`
    : window.location.origin,
};
