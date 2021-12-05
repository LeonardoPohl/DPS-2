import { createContext } from 'react';

export interface ModalData {
  title?: string;
  text?: string;
  okButtonText?: string;
  onOk?: () => void;
  onCancel?: () => void;
}

export const ModalContext = createContext<{
  data: ModalData;
  update: (d: ModalData) => void;
} | null>(null);
