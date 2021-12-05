import React from "react";
import ReactDOM from "react-dom";
import App from "./components/app/app";
import "./index.scss";
import reportWebVitals from "./reportWebVitals";

import Worker from "workerize-loader!./worker.ts"; // eslint-disable-line import/no-webpack-loader-syntax
for (let i = 0; i < 8; i++) {
  const worker = new Worker();
  // Create an instance of your worker
  // Attach an event listener to receive calculations from your worker
  worker.addEventListener("message", (message) => {
    console.log("New Message: ", message.data);
  });
  // Run your calculations
  (worker as any).calculatePrimes(i);
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
