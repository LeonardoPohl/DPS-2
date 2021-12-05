import ReactModal from 'react-modal';
import './modal.scss';
import exitUri from '../../assets/exit.svg';
import { useContext } from 'react';
import { ModalContext } from '../../contexts/modal-context';

ReactModal.defaultStyles.overlay!.backgroundColor = 'rgba(255, 255, 255, 0.5)';
ReactModal.defaultStyles.overlay!.backdropFilter = 'blur(16px)';
ReactModal.defaultStyles.overlay!.zIndex = 10000;

const Modal = () => {
  const { data, update } = useContext(ModalContext)!;

  const cancel = () => {
    data.onCancel?.();
    update({});
  };

  const ok = () => {
    data.onOk?.();
    update({});
  };

  return (
    <ReactModal
      isOpen={!!data.text || !!data.title}
      onRequestClose={() => cancel()}
      className="modal"
      ariaHideApp={false}
      contentLabel="Message"
    >
      <header>
        <h2>{data.title}</h2>
        <img className="exit" alt="exit" src={exitUri} onClick={() => cancel()} />
      </header>
      <p>{data.text}</p>
      {data.onOk && <button onClick={() => ok()}>{data.okButtonText ?? 'Yes'}</button>}
    </ReactModal>
  );
};

export default Modal;
