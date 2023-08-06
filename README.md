# fastMovie

## Features

- **FastAPI** with Python 3.8
- **React 16** with Typescript, Redux, and react-router
- Postgres
- SqlAlchemy with Alembic for migrations
- Pytest for backend tests
- Jest for frontend tests
- Perttier/Eslint (with Airbnb style guide)
- Docker compose for easier development
- Nginx as a reverse proxy to allow backend and frontend on the same port

## Development

The only dependencies for this project should be docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
docker-compose up -d
```

To run the alembic migrations (for the users table):

```bash
docker-compose run --rm backend alembic upgrade head
```

And navigate to http://localhost:8000

_Note: If you see an Nginx error at first with a `502: Bad Gateway` page, you may have to wait for webpack to build the development server (the nginx container builds much more quickly)._

Auto-generated docs will be at
http://localhost:8000/api/docs

### Rebuilding containers:

```
docker-compose build
```

### Restarting containers:

```
docker-compose restart
```

### Bringing containers down:

```
docker-compose down
```

### Frontend Development

Alternatively to running inside docker, it can sometimes be easier
to use npm directly for quicker reloading. To run using npm:

```
cd frontend
npm install
npm start
```

This should redirect you to http://localhost:3000

### Frontend Tests

```
cd frontend
npm install
npm test
```

## Migrations

Migrations are run using alembic. To run all migrations:

```
docker-compose run --rm backend alembic upgrade head
```

To create a new migration:

```
alembic revision -m "create users table"
```

And fill in `upgrade` and `downgrade` methods. For more information see
[Alembic's official documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script).

## Testing

There is a helper script for both frontend and backend tests:

```
./scripts/test.sh
```

### Backend Tests

```
docker-compose run backend pytest
```

any arguments to pytest can also be passed after this command

### Frontend Tests

```
docker-compose run frontend test
```

This is the same as running npm test from within the frontend directory

## Logging

```
docker-compose logs
```

Or for a specific service:

```
docker-compose logs -f name_of_service # frontend|backend|db
```

## Project Layout

```
backend
└── app
    ├── alembic
    │   └── versions # where migrations are located
    ├── api
    │   └── api_v1
    │       └── endpoints
    ├── core    # config
    ├── db      # db models
    ├── tests   # pytest
    └── main.py # entrypoint to backend

frontend
└── public
└── src
    ├── components
    │   └── Home.tsx
    ├── config
    │   └── index.tsx   # constants
    ├── __tests__
    │   └── test_home.tsx
    ├── index.tsx   # entrypoint
    └── App.tsx     # handles routing
```

```
fastMovie
├─ .prettierignore
├─ backend
│  ├─ alembic.ini
│  ├─ app
│  │  ├─ alembic
│  │  │  ├─ env.py
│  │  │  ├─ README
│  │  │  ├─ script.py.mako
│  │  │  ├─ versions
│  │  │  │  └─ 91979b40eb38_create_users_table.py
│  │  │  └─ __init__.py
│  │  ├─ alembic.ini
│  │  ├─ api
│  │  │  ├─ api_v1
│  │  │  │  ├─ routers
│  │  │  │  │  ├─ auth.py
│  │  │  │  │  ├─ tests
│  │  │  │  │  │  ├─ test_auth.py
│  │  │  │  │  │  ├─ test_users.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ users.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ dependencies
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ core
│  │  │  ├─ auth.py
│  │  │  ├─ celery_app.py
│  │  │  ├─ config.py
│  │  │  ├─ security.py
│  │  │  └─ __init__.py
│  │  ├─ db
│  │  │  ├─ crud.py
│  │  │  ├─ models.py
│  │  │  ├─ schemas.py
│  │  │  ├─ session.py
│  │  │  └─ __init__.py
│  │  ├─ initial_data.py
│  │  ├─ main.py
│  │  ├─ tasks.py
│  │  ├─ tests
│  │  │  ├─ test_main.py
│  │  │  ├─ test_tasks.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ conftest.py
│  ├─ Dockerfile
│  ├─ pyproject.toml
│  └─ requirements.txt
├─ docker-compose.yml
├─ frontend
│  ├─ .dockerignore
│  ├─ .eslintrc.js
│  ├─ .prettierrc.js
│  ├─ Dockerfile
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.ico
│  │  ├─ index.html
│  │  ├─ logo192.png
│  │  ├─ logo512.png
│  │  ├─ manifest.json
│  │  └─ robots.txt
│  ├─ README.md
│  ├─ run.sh
│  ├─ src
│  │  ├─ admin
│  │  │  ├─ Admin.tsx
│  │  │  ├─ authProvider.ts
│  │  │  ├─ index.ts
│  │  │  └─ Users
│  │  │     ├─ index.ts
│  │  │     ├─ UserCreate.tsx
│  │  │     ├─ UserEdit.tsx
│  │  │     └─ UserList.tsx
│  │  ├─ App.tsx
│  │  ├─ config
│  │  │  └─ index.tsx
│  │  ├─ decs.d.ts
│  │  ├─ index.css
│  │  ├─ index.tsx
│  │  ├─ logo.svg
│  │  ├─ react-app-env.d.ts
│  │  ├─ Routes.tsx
│  │  ├─ utils
│  │  │  ├─ api.ts
│  │  │  ├─ auth.ts
│  │  │  └─ index.ts
│  │  ├─ views
│  │  │  ├─ Home.tsx
│  │  │  ├─ index.ts
│  │  │  ├─ Login.tsx
│  │  │  ├─ PrivateRoute.tsx
│  │  │  ├─ Protected.tsx
│  │  │  └─ SignUp.tsx
│  │  └─ __tests__
│  │     ├─ home.test.tsx
│  │     └─ login.test.tsx
│  └─ tsconfig.json
├─ nginx
│  └─ nginx.conf
├─ README.md
└─ scripts
   ├─ build.sh
   ├─ test.sh
   └─ test_backend.sh

```