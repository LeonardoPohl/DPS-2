import { RequestOptions } from "./requests/request-options";
import { config } from "../config";

const { baseUri } = config;

export const sendRequest = async <T>(
  request: RequestOptions
): Promise<T | null> => {
  const headers: any = {};

  if (request.payload) {
    headers["Content-Type"] = "application/json";
  }

  try {
    const response = await fetch(baseUri + request.uri, {
      method: request.method,
      mode: "cors",
      headers,
      body: JSON.stringify(request.payload),
    });

    return await response.json();
  } catch {
    return null;
  }
};
