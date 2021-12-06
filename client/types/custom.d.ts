declare module "workerize-loader!*" {
  class WebpackWorker extends Worker {
    constructor();

    execute(
      workerId: number,
      script: string,
      context: { [key: string]: any }
    ): Promise<any>;
  }

  export = WebpackWorker;
}
