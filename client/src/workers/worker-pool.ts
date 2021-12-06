import Worker from "workerize-loader!./worker.ts"; // eslint-disable-line import/no-webpack-loader-syntax

export class WorkerPool {
  private workers: Array<Worker> = [];
  private doneSinceLastCheck = 0;
  private sourceCodePromise = fetch("/worker.py");
  private workerSourceCode: string | null = null;

  public constructor(
    private webSocketAddress: string,
    private onError: (e: string) => unknown
  ) {}

  public async setWorkerCount(count: number) {
    const result = await this.sourceCodePromise;
    if (!this.workerSourceCode) {
      this.workerSourceCode = await result.text();
    }

    const delta = count - this.workers.length;

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
        worker.execute(this.workers.length, this.workerSourceCode, {
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
