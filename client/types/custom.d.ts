declare module "workerize-loader!*" {
  class WebpackWorker extends Worker {
    constructor();
    execute(workerId: number, script: string): Promise<any>;
  }

  export = WebpackWorker;
}
