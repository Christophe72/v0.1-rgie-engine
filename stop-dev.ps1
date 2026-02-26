$ErrorActionPreference = 'SilentlyContinue'

function Stop-PortProcess {
    param([int]$Port)

    $processIds = Get-NetTCPConnection -LocalPort $Port -State Listen |
        Select-Object -ExpandProperty OwningProcess -Unique

    foreach ($processId in $processIds) {
        if ($processId) {
            Stop-Process -Id $processId -Force
        }
    }
}

Stop-PortProcess -Port 8000
Stop-PortProcess -Port 3000

Write-Host 'Ports stoppés : 8000 (backend) et 3000 (frontend).'
