const vscode = require("vscode");

function activate(context) {
  const disposable = vscode.commands.registerCommand("nython.runCurrentFile", () => {
    const editor = vscode.window.activeTextEditor;

    if (!editor) {
      vscode.window.showWarningMessage("No hay un archivo abierto.");
      return;
    }

    const fileName = editor.document.fileName;
    const terminal = vscode.window.createTerminal("Ñython");
    terminal.show();
    terminal.sendText(`nython ejecutar "${fileName}"`);
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
