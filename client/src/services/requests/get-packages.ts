import { RequestOptions } from "./request-options";

export const getPackages = (): RequestOptions => ({
  method: "GET",
  uri: `packages`,
});
