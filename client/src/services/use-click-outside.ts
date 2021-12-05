import { useMemo, useEffect, useRef } from 'react';

export const useClickOutside = <T extends HTMLElement>(
  callback: () => unknown,
): React.MutableRefObject<T> => {
  const ref = useRef<T>(null) as React.MutableRefObject<T>;

  const handleOutsideClick = useMemo(
    () => (e: Event) => {
      if (ref && !ref.current?.contains(e.target as Node)) {
        callback();
      }
    },
    [ref, callback],
  );

  useEffect(() => {
    document.addEventListener('click', handleOutsideClick);
    return () => document.removeEventListener('click', handleOutsideClick);
  }, [handleOutsideClick]);

  return ref;
};
