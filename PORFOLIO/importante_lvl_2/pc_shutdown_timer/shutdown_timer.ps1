# Configuración para ocultar la ventana del cmd al ejecutar el script
Add-Type -TypeDefinition @"
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
public class ConsoleManager {
    [DllImport("kernel32.dll")]
    public static extern IntPtr GetConsoleWindow();

    [DllImport("user32.dll")]
    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

    public const int SW_HIDE = 0;
    public const int SW_SHOW = 5;

    public static void HideConsoleWindow() {
        var handle = GetConsoleWindow();
        if (handle != IntPtr.Zero) {
            ShowWindow(handle, SW_HIDE);
        }
    }
}
"@
[ConsoleManager]::HideConsoleWindow()

# Cargar bibliotecas necesarias
Add-Type -AssemblyName Microsoft.VisualBasic
Add-Type -AssemblyName System.Windows.Forms

# Configurar alta calidad para cuadros de diálogo
[System.Windows.Forms.Application]::EnableVisualStyles()

# Solicitar tiempo en minutos usando un cuadro de diálogo
$timeInput = [Microsoft.VisualBasic.Interaction]::InputBox(
    "¿En cuántos minutos desea apagar el PC?", 
    "Temporizador de Apagado", 
    "5"
)

# Validar si el tiempo ingresado es un número válido
if (![int]::TryParse($timeInput, [ref]$null)) {
    [System.Windows.Forms.MessageBox]::Show(
        "Por favor, ingrese un número válido.", 
        "Error", 
        [System.Windows.Forms.MessageBoxButtons]::OK, 
        [System.Windows.Forms.MessageBoxIcon]::Error
    )
    exit
}

# Convertir minutos a segundos
$timeInSeconds = [int]$timeInput * 60

# Confirmar el tiempo de apagado
[System.Windows.Forms.MessageBox]::Show(
    "Tu PC se apagará en $timeInput minutos.", 
    "Confirmación", 
    [System.Windows.Forms.MessageBoxButtons]::OK, 
    [System.Windows.Forms.MessageBoxIcon]::Information
)

# Ejecutar el comando de apagado directamente
Start-Process -FilePath "shutdown" -ArgumentList "/s /t $timeInSeconds" -WindowStyle Hidden

# Temporizador para la cancelación
Start-Sleep -Seconds ($timeInSeconds - 15)

# Mostrar cuadro para cancelar el apagado
$cancel = [System.Windows.Forms.MessageBox]::Show(
    "Quedan 15 segundos para que se apague el equipo. ¿Deseas cancelar?", 
    "Cancelar Apagado", 
    [System.Windows.Forms.MessageBoxButtons]::YesNo, 
    [System.Windows.Forms.MessageBoxIcon]::Warning
)

# Si se selecciona "Sí", cancelar el apagado
if ($cancel -eq [System.Windows.Forms.DialogResult]::Yes) {
    Start-Process -FilePath "shutdown" -ArgumentList "/a" -WindowStyle Hidden
    [System.Windows.Forms.MessageBox]::Show(
        "El apagado ha sido cancelado.", 
        "Cancelado", 
        [System.Windows.Forms.MessageBoxButtons]::OK, 
        [System.Windows.Forms.MessageBoxIcon]::Information
    )
}
