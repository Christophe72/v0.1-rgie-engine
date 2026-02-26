# WebElec RGIE Engine

Monorepo avec :
- un **backend FastAPI** (`backend/`) pour exposer les règles RGIE,
- un **frontend Next.js** (`frontend/`) pour afficher les règles.

## Structure du projet

```text
webelec-rgie/
├── backend/
│   ├── app/
│   │   ├── core/config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routers/
│   │   │   ├── health.py
│   │   │   └── rules.py
│   │   ├── schemas.py
│   │   └── seed.py
│   ├── .env
│   └── .venv/
├── frontend/
│   ├── app/page.tsx
│   ├── .env.local
│   └── package.json
├── start-dev.ps1
└── stop-dev.ps1
```

## Prérequis

- **Python 3.12+** (venv backend)
- **Node.js 20+** + npm (frontend)
- **PostgreSQL** accessible depuis `DATABASE_URL`
- Windows PowerShell (scripts fournis)

## Variables d’environnement

### Backend (`backend/.env`)

Exemple minimal :

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/webelec
```

### Frontend (`frontend/.env.local`)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Démarrage rapide (recommandé)

Depuis la racine du repo :

```powershell
.\start-dev.ps1
```

Ce script :
- libère les ports `8000` (backend) et `3000` (frontend),
- supprime le lock Next.js éventuel,
- ouvre 2 terminaux : backend + frontend.

Arrêter les deux services :

```powershell
.\stop-dev.ps1
```

## Lancement manuel

### 1) Backend

```powershell
cd c:\saas\webelec-rgie\backend
.\.venv\Scripts\python.exe -m pip install -r app\requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 --app-dir c:\saas\webelec-rgie\backend
```

### 2) Frontend

```powershell
cd c:\saas\webelec-rgie\frontend
npm install
npm run dev
```

## API disponible

Base URL: `http://127.0.0.1:8000`

- `GET /health` → statut de santé API
- `GET /rules/` → liste des règles
- `POST /rules/` → création d’une règle

### Exemple `POST /rules/`

```json
{
	"code": "RGIE-001",
	"title": "Titre de la règle",
	"description": "Description",
	"legal_reference": "Art. X",
	"is_new": true,
	"metadata": {
		"source": "manual"
	}
}
```

## Notes techniques

- Le backend crée automatiquement le schéma PostgreSQL `rgie` au démarrage.
- Le seed est exécuté au startup FastAPI (via `lifespan`).
- Le frontend lit l’API via `NEXT_PUBLIC_API_URL` avec fallback sur `http://localhost:8000`.
