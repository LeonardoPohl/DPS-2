import React, { useEffect, useState } from "react";
import { ModalContext, ModalData } from "../../contexts/modal-context";
import "./app.scss";
import Modal from "../modal/modal";
import HasFooter from "../footer/has-footer";
import { config } from "../../config";
import {
  LineChart,
  Line,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { WorkerPool } from "../../workers/worker-pool";

const yName = "Tasks completed per second";

const App = () => {
  const [modalValue, setModalValue] = useState<ModalData>({});
  const [processCount, setProcessCount] = useState(1);
  const [doneCounts, setDoneCounts] = useState<Array<{ [yName]: number }>>([]);
  const [pool, setPool] = useState<WorkerPool | null>(null);

  useEffect(() => {
    setPool(
      new WorkerPool(config.webSocketAddress, (e) =>
        setModalValue({
          title: "Error",
          text: e,
        })
      )
    );
  }, []);

  useEffect(() => {
    const id = setInterval(
      () =>
        setDoneCounts((v) => [
          ...v.slice(-20),
          { [yName]: pool!.checkDoneCount() },
        ]),
      1000
    );

    return () => clearInterval(id);
  }, [pool]);

  useEffect(() => {
    pool?.setWorkerCount(processCount);
  }, [processCount, pool]);

  const longestLabelLength = doneCounts
    .map((c) => c[yName].toString())
    .reduce((acc, cur) => (cur.length > acc ? cur.length : acc), 0);

  return (
    <ModalContext.Provider value={{ data: modalValue, update: setModalValue }}>
      <Modal />
      <main>
        <HasFooter>
          <header>
            <h1>Nitocris</h1>
            <h2>Client</h2>
          </header>

          <div className="main-wrapper">
            <section>
              <div className="config">
                <label htmlFor="process-count">Process count</label>
                <input
                  type="number"
                  name="process count"
                  min="0"
                  max="32"
                  step="1"
                  id="process-count"
                  value={processCount}
                  onChange={(e) =>
                    setProcessCount(Number.parseInt(e.target.value))
                  }
                />
              </div>
              <div className="chart">
                <ResponsiveContainer height={300} width="100%">
                  <LineChart data={doneCounts}>
                    <YAxis width={longestLabelLength * 13} />
                    <Legend
                      verticalAlign="top"
                      wrapperStyle={{
                        paddingBottom: "20px",
                      }}
                    />
                    <Tooltip />
                    <Line
                      dataKey={yName}
                      type="monotone"
                      fill="#8884d8"
                      animationDuration={0}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </section>
          </div>
        </HasFooter>
      </main>
    </ModalContext.Provider>
  );
};

export default App;
