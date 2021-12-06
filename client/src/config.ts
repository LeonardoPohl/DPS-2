import { isDevelopment } from "./helper/is-development";

export const config = {
  webSocketAddress: isDevelopment
    ? "ws://localhost:7700"
    : "https://backend.party-rhythm.ml/",
  baseUri: "",
};
