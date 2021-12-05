/* eslint-disable no-restricted-globals */

(self as any).importScripts(
  "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/pyodide.js"
);

async function loadPyodideAndPackages() {
  (self as any).pyodide = await (self as any).loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
  });
}

let pyodideReadyPromise = loadPyodideAndPackages();

export const execute = async (workerId: number, script: string) => {
  postMessage(`Hi from ${workerId}`);

  await pyodideReadyPromise;

  try {
    await (self as any).pyodide.loadPackagesFromImports(script);
    let results = await (self as any).pyodide.runPythonAsync(script);
    self.postMessage({ results });
  } catch (error: any) {
    self.postMessage({ error: error.message });
  }
};

self.onmessage = async (event) => {};
