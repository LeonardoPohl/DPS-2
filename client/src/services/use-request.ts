import { useEffect, useRef, useState } from 'react';
import { RequestOptions } from './requests/request-options';
import { sendRequest } from './send-request';

export const useRequest = <T>(request: RequestOptions) => {
  const isCurrent = useRef(true);

  const [refresh, setRefresh] = useState(0);

  const [state, setState] = useState<
    {
      data: T | null;
      loading: boolean;
    } & { refresh: () => void }
  >({
    data: null,
    loading: true,
    refresh: () => setRefresh((r) => r + 1),
  });

  useEffect(() => {
    return () => {
      isCurrent.current = false;
    };
  }, []);

  useEffect(() => {
    setState((s) => ({
      ...s,
      loading: true,
    }));

    if (!request.invalid) {
      sendRequest<T>(request).then((json) => {
        if (isCurrent.current) {
          setState((s) => ({
            ...s,
            data: json!,
            loading: false,
          }));
        }
      });
    } else {
      setState((s) => ({
        ...s,
        data: null,
        loading: false,
      }));
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [setState, request.method, request.invalid, request.payload, request.uri, refresh]);

  return state;
};
