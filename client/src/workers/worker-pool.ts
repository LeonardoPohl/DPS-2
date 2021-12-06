import Worker from "workerize-loader!./worker.ts"; // eslint-disable-line import/no-webpack-loader-syntax
import { config } from "../config";
import { getPackages } from "../services/requests/get-packages";
import { sendRequest } from "../services/send-request";

export class WorkerPool {
  private workers: Array<Worker> = [];
  private doneSinceLastCheck = 0;
  private sourceCodePromise = fetch("/worker.py");
  private workerSourceCode: string | null = null;
  private webSocketAddress: string;

  public constructor(private onError: (e: string) => unknown) {
    this.webSocketAddress = `ws://${window.location.hostname}:${config.webSocketPort}`;
  }

  private async preprocessSourceCode() {
    const result = await this.sourceCodePromise;

    const dependencies = (await sendRequest<Array<string>>(getPackages()))!;

    if (!this.workerSourceCode) {
      let text = await result.text();
      const dependencyInstallCode = dependencies
        .map((d) => `await micropip.install('${d}')`)
        .join("\n");

      text = text.replace("!!INSTALL_DEPENDENCIES!!", dependencyInstallCode);
      this.workerSourceCode = text;
    }
  }

  public async setWorkerCount(count: number) {
    const delta = count - this.workers.length;

    await this.preprocessSourceCode();
    if (delta < 0) {
      for (let i = 0; i > delta; i--) {
        const worker = this.workers.pop();
        worker!.terminate();
      }
    } else if (delta > 0) {
      for (let i = 0; i < delta; i++) {
        const worker = new Worker();
        worker.onerror = (e) => this.onError(e.message);
        worker.onmessage = (m) => {
          if (m.data.done) {
            this.doneSinceLastCheck++;
          }
          if (m.data.error) {
            this.onError(m.data.error);
          }
        };
        worker.execute(this.workers.length, this.workerSourceCode!, {
          webSocketAddress: this.webSocketAddress,
        });
        this.workers.push(worker);
      }
    }
  }

  public checkDoneCount(): number {
    const temp = this.doneSinceLastCheck;
    this.doneSinceLastCheck = 0;
    return temp;
  }
}
