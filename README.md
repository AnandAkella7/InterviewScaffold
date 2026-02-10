# Interview Scaffold Cheat Sheet

## 1. Start Backend (Port 8000)
Run this in a terminal inside `interview-scaffold/backend`:
```powershell
.\run.bat
```
*   **Health Check:** <http://localhost:8000/>
*   **GraphQL:** <http://localhost:8000/graphql>

### OR run manually (standard way):
1.  `.\venv\Scripts\activate` (You will see `(venv)` in prompt)
2.  `python main.py`

## 2. Start Frontend (Port 3001)
Run this in a **new** terminal inside `interview-scaffold/frontend`:
```powershell
npx vite
```
*   **App URL:** <http://localhost:3001/>

## troubleshooting
If `npx vite` fails, try:
```powershell
npx vite --force
```
If port 3001 is somehow blocked, try:
```powershell
npx vite --port 3002
```

## 3. Stopping Servers
*   **Standard Way:** Click inside the terminal and press `Ctrl + C`. It will ask "Terminate batch job (Y/N)?", type `y` and Enter.
*   **Force Kill (if stuck):**
    ```powershell
    Stop-Process -Name python -Force
    Stop-Process -Name node -Force
    ```
