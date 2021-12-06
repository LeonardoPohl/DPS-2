/* eslint-disable no-restricted-globals */

(self as any).importScripts(
  "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/pyodide.js"
);

async function loadPyodideAndPackages() {
  (self as any).pyodide = await (self as any).loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
  });

  await (self as any).pyodide.loadPackage(["micropip"]);
}

let pyodideReadyPromise = loadPyodideAndPackages();

export const execute = async (
  workerId: number,
  script: string,
  context: { [key: string]: any }
) => {
  postMessage(`Worker ${workerId} started`);

  await pyodideReadyPromise;

  context.onFinished = () => self.postMessage({ done: 1 });
  for (const key of Object.keys(context)) {
    (self as any)[key] = context[key];
  }

  try {
    await (self as any).pyodide.loadPackagesFromImports(script);
    const results = await (self as any).pyodide.runPythonAsync(script);
    self.postMessage({ results });
  } catch (error: any) {
    self.postMessage({ error: error.message });
  }
};
