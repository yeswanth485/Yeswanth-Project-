$files = @("server.py", "index.html", "seed_data.py", "docker-compose.yml")
$Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False

foreach ($file in $files) {
    $path = Join-Path "d:\Final-year-project-main" $file
    if (Test-Path $path) {
        $content = Get-Content $path -Raw
        [System.IO.File]::WriteAllText($path, $content, $Utf8NoBomEncoding)
        Write-Output "Fixed encoding for $file"
    }
}
