$ErrorActionPreference = 'SilentlyContinue'

$root = 'c:\saas\webelec-rgie'
$backendDir = Join-Path $root 'backend'
$frontendDir = Join-Path $root 'frontend'
$backendPython = Join-Path $backendDir '.venv\Scripts\python.exe'

function Stop-PortProcess {
    param([int]$Port)

    $pids = Get-NetTCPConnection -LocalPort $Port -State Listen | Select-Object -ExpandProperty OwningProcess -Unique
    foreach ($processId in $pids) {
        if ($processId) {
            Stop-Process -Id $processId -Force
        }
    }
}

Stop-PortProcess -Port 8000
Stop-PortProcess -Port 3000

Remove-Item (Join-Path $frontendDir '.next\dev\lock') -Force

$backendCommand = "Set-Location '$backendDir'; & '$backendPython' -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 --app-dir '$backendDir'"
$frontendCommand = "Set-Location '$frontendDir'; npm run dev"

Start-Process powershell -ArgumentList '-NoExit', '-Command', $backendCommand | Out-Null
Start-Process powershell -ArgumentList '-NoExit', '-Command', $frontendCommand | Out-Null

Write-Host 'Backend: http://127.0.0.1:8000'
Write-Host 'Frontend: http://127.0.0.1:3000'
Write-Host 'Deux terminaux ont été ouverts.'
