import { isDevelopment } from './helper/is-development';

export const config = {
  baseUri: isDevelopment ? 'http://localhost:5050/' : 'https://backend.party-rhythm.ml/',
  dashboardUri: isDevelopment ? 'http://localhost:3000/' : 'https://party-rhythm.ml/',
  localStorageKeyForUserId: 'user-id',
  spotifyClientId: '9729a203e95a4d3f93fe39560404bf19',
};
