@echo off
title Atualizar edenEquips
setlocal

echo ===============================
echo   Atualizador do edenEquips
echo ===============================
echo.

REM Chama o script PowerShell na mesma pasta deste .bat
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0atualizar-edenEquips.ps1"

if errorlevel 1 (
    echo.
    echo Ocorreu um erro ao atualizar o edenEquips.
    echo Verifique sua conexao com a internet ou tente novamente mais tarde.
    echo.
    pause
)

endlocal
