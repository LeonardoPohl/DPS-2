import { isDevelopment } from "./helper/is-development";

export const config = {
  webSocketPort: 7700,
  baseUri: `${window.location.protocol}//${window.location.hostname}:7701`,
};
