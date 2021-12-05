import React, { useState } from "react";
import { ModalContext, ModalData } from "../../contexts/modal-context";
import "./app.scss";
import Modal from "../modal/modal";
import HasFooter from "../footer/has-footer";

const App = () => {
  const [modalValue, setModalValue] = useState<ModalData>({});

  return (
    <ModalContext.Provider value={{ data: modalValue, update: setModalValue }}>
      <Modal />
      <HasFooter>hi</HasFooter>
    </ModalContext.Provider>
  );
};

export default App;
