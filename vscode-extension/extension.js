const vscode = require("vscode");

function archivoActivo() {
  const editor = vscode.window.activeTextEditor;

  if (!editor) {
    vscode.window.showWarningMessage("No hay un archivo abierto.");
    return null;
  }

  return editor.document.fileName;
}

function terminalNython() {
  const terminal = vscode.window.createTerminal("Ñython");
  terminal.show();
  return terminal;
}

function activate(context) {
  const run = vscode.commands.registerCommand("nython.runCurrentFile", () => {
    const fileName = archivoActivo();
    if (!fileName) {
      return;
    }
    terminalNython().sendText(`nython ejecutar "${fileName}"`);
  });

  const translate = vscode.commands.registerCommand("nython.translateCurrentFile", () => {
    const fileName = archivoActivo();
    if (!fileName) {
      return;
    }
    terminalNython().sendText(`nython traducir "${fileName}"`);
  });

  const compile = vscode.commands.registerCommand("nython.compileCurrentFile", () => {
    const fileName = archivoActivo();
    if (!fileName) {
      return;
    }
    const output = fileName.replace(/\.(ny|nython)$/i, ".py");
    terminalNython().sendText(`nython compilar "${fileName}" -o "${output}"`);
  });

  context.subscriptions.push(run, translate, compile);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
