

# fastapi_movie_app

This project was generated using fastapi_template.

- first create conda environment

conda create -n fastapi_movie_app python=3.9

- activate environment

conda activate fastapi_movie_app

- conda install from txt file

conda install --file conda_fastApi_packages.txt


This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m fastapi_movie_app
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "fastapi_movie_app"
fastapi_movie_app
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "FASTAPI_MOVIE_APP_" prefix.

For example if you see in your "fastapi_movie_app/settings.py" a variable named like
`random_parameter`, you should provide the "FASTAPI_MOVIE_APP_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `fastapi_movie_app.settings.Settings.Config`.

An example of .env file:
```bash
FASTAPI_MOVIE_APP_RELOAD="True"
FASTAPI_MOVIE_APP_PORT="8000"
FASTAPI_MOVIE_APP_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);


You can read more about pre-commit here: https://pre-commit.com/

## Migrations

If you want to migrate your database, you should run following commands:
```bash
# To run all migrations until the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### Reverting migrations

If you want to revert migrations, you should run:
```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
 alembic downgrade base
```

### Migration generation

To generate migrations you should run:
```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.
1. you need to start a database.

I prefer doing it with docker:
```
docker run -p "5432:5432" -e "POSTGRES_PASSWORD=fastapi_movie_app" -e "POSTGRES_USER=fastapi_movie_app" -e "POSTGRES_DB=fastapi_movie_app" postgres:13.8-bullseye
```


2. Run the pytest.
```bash
pytest -vv .
```

```
fastapi_movie_app,
├─ .dockerignore,
├─ .editorconfig,
├─ .flake8,
├─ .git,
│  ├─ COMMIT_EDITMSG,
│  ├─ HEAD,
│  ├─ branches,
│  ├─ config,
│  ├─ description,
│  ├─ hooks,
│  │  ├─ applypatch-msg.sample,
│  │  ├─ commit-msg.sample,
│  │  ├─ fsmonitor-watchman.sample,
│  │  ├─ post-update.sample,
│  │  ├─ pre-applypatch.sample,
│  │  ├─ pre-commit,
│  │  ├─ pre-commit.sample,
│  │  ├─ pre-merge-commit.sample,
│  │  ├─ pre-push.sample,
│  │  ├─ pre-rebase.sample,
│  │  ├─ pre-receive.sample,
│  │  ├─ prepare-commit-msg.sample,
│  │  └─ update.sample,
│  ├─ index,
│  ├─ info,
│  │  └─ exclude,
│  ├─ logs,
│  │  ├─ HEAD,
│  │  └─ refs,
│  │     └─ heads,
│  │        └─ master,
│  ├─ objects,
│  │  ├─ 00,
│  │  │  ├─ 434dd4b23a3f98bb0113ab2dcb18e1177cf4f1,
│  │  │  └─ ce79b200091d47e826608299284577052d9e39,
│  │  ├─ 01,
│  │  │  └─ bbbc53e3d70cdcbdd7e7591628d79dbd0ce99b,
│  │  ├─ 02,
│  │  │  └─ 9232b31abce82ff65e7d1b09c89139868a45ed,
│  │  ├─ 04,
│  │  │  └─ 952b98b98983b952de0bf948a607e57d187458,
│  │  ├─ 05,
│  │  │  ├─ 427f6fb3eacaefc57eaa38490a7f57bb78c486,
│  │  │  └─ 840a4a336865561a6d5c3cbe78cc0b470a4080,
│  │  ├─ 09,
│  │  │  └─ c74cd0a90df52e4e3f135174d470a82a667e5e,
│  │  ├─ 0c,
│  │  │  └─ be1af2011da2ad0db103743096d6ab4796b6bc,
│  │  ├─ 0d,
│  │  │  └─ 07b43f1c0c893ae4c018d822b87ffb0db826aa,
│  │  ├─ 0e,
│  │  │  ├─ 3abfa7141eb9774a1a5e84ad06c729c0542410,
│  │  │  └─ d1bef3ed96daae3e608e52d3df70fbe9f1defc,
│  │  ├─ 0f,
│  │  │  └─ 6e53b96925671cd2a630f59542fb5420b0478c,
│  │  ├─ 10,
│  │  │  └─ b74ff4709b7ce4b204802b8f91ccc712ded589,
│  │  ├─ 12,
│  │  │  └─ 9518d35553b5ad91a45df86a256ba23c6c4216,
│  │  ├─ 14,
│  │  │  └─ d2d256553de0b0f91a49d4d34469fc24301d1d,
│  │  ├─ 16,
│  │  │  ├─ 55b9b753905671b0c42e599a5cd1c35a342554,
│  │  │  └─ 7afe917f34897eca4a78e4a60ca1cf69df0e93,
│  │  ├─ 1a,
│  │  │  └─ fa9082f04b2ad41f072406141305e2c0abf1f8,
│  │  ├─ 1b,
│  │  │  └─ 36caf02a1f123eff7d56045b87f820a0cdb8e6,
│  │  ├─ 1f,
│  │  │  └─ 1bea701cc03339d3469c25710639147243b7c0,
│  │  ├─ 25,
│  │  │  └─ 255a585bb45e87f578845a9d02f53f439d3d4a,
│  │  ├─ 26,
│  │  │  └─ 6fa181d2b0b0751cd655f1cb7875cf8acf829d,
│  │  ├─ 28,
│  │  │  └─ ea5ead052109e530675e5ddaaae03b1fb06735,
│  │  ├─ 30,
│  │  │  └─ efeaab063bddedd54e5efdfd25f616077c6dda,
│  │  ├─ 32,
│  │  │  └─ e84a38efc8ebc02a2b213c9c5e1b232ec56788,
│  │  ├─ 34,
│  │  │  └─ 28a9c57cb291c9a910f8c93717d013d9fc0d1b,
│  │  ├─ 35,
│  │  │  ├─ 172c30e07df067fd935a629b8dcca5506fc8a4,
│  │  │  └─ 79f1536848d73ce86d457db297317035018b05,
│  │  ├─ 36,
│  │  │  ├─ 8994ffd63a4e81346cd877817213a23ba6f496,
│  │  │  └─ f92bee11e1fc1e11b2c560cf86d9ab18462d70,
│  │  ├─ 39,
│  │  │  └─ 62e5c792b6d7a5e45a9cdbe690748f64d5776e,
│  │  ├─ 3a,
│  │  │  ├─ 7f1b89e7dd8b2f8b5770a5f1c657f4e9721776,
│  │  │  ├─ a1bee1bb63a7141fe7e924cd3d7a0eb3510972,
│  │  │  ├─ de9423b21c5c026fc22cde600de426f9b3d1b9,
│  │  │  └─ fb361cb2b40c55e432bdbb8aa7ae1f1a6a692d,
│  │  ├─ 3b,
│  │  │  └─ 22742ecaddccd9bef02c4f15a23b9ade7d531d,
│  │  ├─ 40,
│  │  │  └─ 0ee9d7afc91fc16de4c7184452b406a2fff459,
│  │  ├─ 42,
│  │  │  └─ 09439d1da3861b314e96fffb649c16d33c8630,
│  │  ├─ 46,
│  │  │  └─ 3964fd18d5b901aa1c723884d29c296606e88b,
│  │  ├─ 47,
│  │  │  ├─ cc8c4c641277165df1cbe4622a742252f331eb,
│  │  │  └─ d9426c57607307cce246bb2fd4c27e758c7953,
│  │  ├─ 4a,
│  │  │  ├─ 3a313e8c8c12c18b100914d1a2d8ec034067b0,
│  │  │  └─ 636e51e1487b45e544f3671fd5b27e30d99cc7,
│  │  ├─ 4c,
│  │  │  └─ 952541a88d0e55b08b7193d4689c7a6b37209c,
│  │  ├─ 4d,
│  │  │  └─ fddf30c0c37bede144b0e220306a69bf0b165b,
│  │  ├─ 4e,
│  │  │  └─ 1064adcf4edad641f0bc5869c9265b5b72bd11,
│  │  ├─ 4f,
│  │  │  └─ 2dcdcb3e0ff6c1644e0d5a3669930f4c48ed64,
│  │  ├─ 50,
│  │  │  └─ be47664d927b78e0a704369957c074af28ba6b,
│  │  ├─ 53,
│  │  │  └─ cfe1293421e1a24ecb3689f077652a932f7af3,
│  │  ├─ 55,
│  │  │  └─ df2863d206fa1678abb4c92e90c45d3f85c114,
│  │  ├─ 59,
│  │  │  └─ 1992359a6a1de379cb9e5362e248d4a3c5ff7e,
│  │  ├─ 5d,
│  │  │  └─ 16e92eb2a30ea821fa7ccddd99cbdd3120cb9b,
│  │  ├─ 62,
│  │  │  └─ a6f4ad3bdfa2de56de2f7266f536b4e57edb68,
│  │  ├─ 69,
│  │  │  └─ f2d1cc55d778451299ee3a67d0badc4b5391c3,
│  │  ├─ 6c,
│  │  │  └─ d53acbcc61c861d663b4575727dc740f312755,
│  │  ├─ 74,
│  │  │  └─ 0a610dfacf8e2d608658e964f4a1713ff71634,
│  │  ├─ 77,
│  │  │  └─ 2a64f79cafef28d9142133bb58cc234efc26bf,
│  │  ├─ 79,
│  │  │  └─ e71d8e807cfc61f0bc6b996493e4f38f15c20b,
│  │  ├─ 7e,
│  │  │  └─ c0d5f729677ab72e723d8940189331a0fe2ce2,
│  │  ├─ 86,
│  │  │  └─ 844163889c19a8797fe0f323a9c5b2a9eb7cc5,
│  │  ├─ 88,
│  │  │  └─ 50c28580e15ed1508417458222fc161c130175,
│  │  ├─ 8c,
│  │  │  └─ 4310a5f883278192267968e8bf9a388f868345,
│  │  ├─ 93,
│  │  │  ├─ 3b049198f00fd1fa3b8ff5c92bf3d6c2d8063e,
│  │  │  └─ 56da52aabc350d4d3c920a1739ac215c06b415,
│  │  ├─ 97,
│  │  │  └─ acae1fd2efc84c44d8f2f497dc1d9787f0149b,
│  │  ├─ 99,
│  │  │  └─ 720637723e3126f0b17f9a0c6ce2da331bbb85,
│  │  ├─ 9a,
│  │  │  └─ 84f6f6fad9d59658bcf8b5f24ef3e2b220402e,
│  │  ├─ 9b,
│  │  │  └─ 9724c01049de5b939a82ee1068baa1f930a97b,
│  │  ├─ a0,
│  │  │  ├─ 4248df8314d7a99e5d0163394655166ed92587,
│  │  │  └─ d48957d3e0dadd30528b4d05edfc16ceff29dc,
│  │  ├─ a2,
│  │  │  ├─ 4449d437f28102cac3720d8c21aa6ea0306ad3,
│  │  │  ├─ 781ca6a3057e1b9aa13c646e3de3e7d0e77f11,
│  │  │  └─ ed45b701e459e2c47f654b6c5a258d40d058f4,
│  │  ├─ a3,
│  │  │  └─ c9318eeaf189b60894d0a4bb8f178923926a98,
│  │  ├─ aa,
│  │  │  ├─ 70da4e58748cb50ad49bc4bdfd59ce4449b078,
│  │  │  └─ b45d8cede0f4bdd180e60bddce0103f419a256,
│  │  ├─ ab,
│  │  │  ├─ 3a24e7f43e76ef78b3e4468cd8aabda0915b1f,
│  │  │  └─ 79eca91326dbc009f6469be3489441605bf6e4,
│  │  ├─ ac,
│  │  │  └─ 67c6ba18b7835c4bba081cb3be7b8ec0c48f10,
│  │  ├─ ad,
│  │  │  └─ af5ed3c59b524f45727d67bccb3b60b4984fbc,
│  │  ├─ ae,
│  │  │  └─ 43f1dd2e30bde1fbd1cde8a12d3207ee516421,
│  │  ├─ b1,
│  │  │  ├─ 0c36803b607038b6b5595e079a89b44471da74,
│  │  │  └─ cb3a18a738ab64858faf1af04b6db636e6d58d,
│  │  ├─ b3,
│  │  │  └─ d713e35ab76486f9ea15d63dba2acc5c3987d0,
│  │  ├─ b6,
│  │  │  └─ 5d22519952ba89d7bf7f1a1a1c832444e69cb9,
│  │  ├─ b8,
│  │  │  └─ 7be1c1520ba798b1df7322ef018027866756e0,
│  │  ├─ bb,
│  │  │  └─ 06c2beb40cc295c1ce67c9fb8e6c00470d06ce,
│  │  ├─ bd,
│  │  │  └─ 002ec6fc3e16b61c8c17f4996c71afbc0b30cc,
│  │  ├─ be,
│  │  │  ├─ 5ebee8785838054d4d0dc491108524e3d26ba8,
│  │  │  └─ b064851eff7eb11820ab9b5f45453dedab4dc4,
│  │  ├─ bf,
│  │  │  └─ d31371c370b46b47eb3a63bdad218571bf2d52,
│  │  ├─ c0,
│  │  │  └─ 6402a7abbd9aabbd003b5dcb79a2ab08fd2e56,
│  │  ├─ c5,
│  │  │  ├─ ad4bbed5335bbe7f563b0e2133f2bd6c1b4bc3,
│  │  │  └─ f8b02284636a071fc01f1a29102214633e8f3e,
│  │  ├─ c7,
│  │  │  └─ 797245453f0e0d19303de6beee32dd1350418f,
│  │  ├─ c8,
│  │  │  └─ de25a0d0d722bd2bcd50eeab9429e609b3e550,
│  │  ├─ c9,
│  │  │  └─ 51b09b519016c6e7dc50fccb107b757db00ef9,
│  │  ├─ cc,
│  │  │  └─ ad150cbae4b191d7c97387871a3abad0472cb2,
│  │  ├─ ce,
│  │  │  └─ 8391a848075b6e3f256f67dd85dec7dd478f44,
│  │  ├─ cf,
│  │  │  └─ 8e17ac77c80068f804c611b337d2827e24459a,
│  │  ├─ d0,
│  │  │  ├─ 2bfec247344ce856ba77ea11e8a0b5b52b397d,
│  │  │  └─ 5e78978cfff44f35883e4d33a81ec2296430d4,
│  │  ├─ d5,
│  │  │  └─ 9a813cfcaf880f37c9d152dfa4bae0d6126b8f,
│  │  ├─ d7,
│  │  │  └─ 5854f11c0997d701fd95aacbc1b0eda59cfdc2,
│  │  ├─ da,
│  │  │  └─ 76f2af1aa7f3d3cb9c6c58ef903c0998767bb9,
│  │  ├─ db,
│  │  │  ├─ 010e174c4e22e6579e1f20bec9f70948e794bc,
│  │  │  └─ 62a0afb2db870dce3368e05380185d0e71bbdc,
│  │  ├─ df,
│  │  │  └─ cab4233a080e7c5b7e47a7428127ce3c0bb96d,
│  │  ├─ e1,
│  │  │  ├─ 06d0b62fbd10031aa8b0b2a2dbc0416b8f0601,
│  │  │  ├─ 0906b8d15ac39a850f15a9776cf17b995920d6,
│  │  │  └─ 5b2498ecf3144f0c13511e3cdf3b51341b0116,
│  │  ├─ e2,
│  │  │  ├─ 6c5e934de6223a176e17149e84bc570b385c1d,
│  │  │  └─ f4fe8dd0b9860b87c54246bccfd01f911a0bda,
│  │  ├─ e4,
│  │  │  └─ 137eb99feb8eedc4ea81f1822580464b8904f7,
│  │  ├─ e6,
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391,
│  │  ├─ e7,
│  │  │  ├─ 2cd90048e2d1920b9de8281a0aea51d974f8bd,
│  │  │  └─ e025d5c99a96ca53a423019c56aa0998901dc1,
│  │  ├─ eb,
│  │  │  ├─ 3f6ad6459255c70776b70af71e4a8e1487502c,
│  │  │  └─ 831fe62fdb60b99f1b29973088e596c7e310ce,
│  │  ├─ f0,
│  │  │  └─ 79f6ed89390f6ee45bdbccb79944a581e613f8,
│  │  ├─ f1,
│  │  │  └─ 988cdeb82edc6c2ffbf1ed25a02b1fb4f03b12,
│  │  ├─ f2,
│  │  │  └─ b8ef587f285cf77c3f5c1639dadae16dbc708a,
│  │  ├─ f4,
│  │  │  ├─ 08bc21d58385637c85049f6e83338bb8c65c32,
│  │  │  └─ 42bb851a1305603f8b8c1d606e48d25e9fb8c3,
│  │  ├─ f6,
│  │  │  └─ 01975ba17e1692db1dfd859eb6b612c420a3d4,
│  │  ├─ f7,
│  │  │  └─ c1a6c526d222680cc2b332497d4ced1dafb3bc,
│  │  ├─ f8,
│  │  │  ├─ 2ef185487ce9c0dbaa425926f6a1b307937d3c,
│  │  │  └─ 5f3558951b88ad46609396d8bb3b0d6c3c7659,
│  │  ├─ f9,
│  │  │  └─ 921ea95cb2a3c4e79943dce2715c72b2d0b0f7,
│  │  ├─ fe,
│  │  │  └─ 6e721b84c9f4824fbbc629f0ad31d20031d27d,
│  │  ├─ info,
│  │  └─ pack,
│  └─ refs,
│     ├─ heads,
│     │  └─ master,
│     └─ tags,
├─ .github,
│  └─ workflows,
│     └─ tests.yml,
├─ .gitignore,
├─ .pre-commit-config.yaml,
├─ README.md,
├─ alembic.ini,
├─ deploy,
│  ├─ Dockerfile,
│  ├─ docker-compose.dev.yml,
│  └─ docker-compose.yml,
├─ fastapi_movie_app,
│  ├─ __init__.py,
│  ├─ __main__.py,
│  ├─ conftest.py,
│  ├─ db,
│  │  ├─ base.py,
│  │  ├─ dao,
│  │  │  ├─ __init__.py,
│  │  │  └─ dummy_dao.py,
│  │  ├─ dependencies.py,
│  │  ├─ meta.py,
│  │  ├─ migrations,
│  │  │  ├─ __init__.py,
│  │  │  ├─ env.py,
│  │  │  ├─ script.py.mako,
│  │  │  └─ versions,
│  │  │     ├─ 2021-08-16-16-53_819cbf6e030b.py,
│  │  │     ├─ 2021-08-16-16-55_2b7380507a71.py,
│  │  │     └─ __init__.py,
│  │  ├─ models,
│  │  │  ├─ __init__.py,
│  │  │  └─ dummy_model.py,
│  │  └─ utils.py,
│  ├─ gunicorn_runner.py,
│  ├─ services,
│  │  ├─ __init__.py,
│  │  ├─ rabbit,
│  │  │  ├─ __init__.py,
│  │  │  ├─ dependencies.py,
│  │  │  └─ lifetime.py,
│  │  └─ redis,
│  │     ├─ __init__.py,
│  │     ├─ dependency.py,
│  │     └─ lifetime.py,
│  ├─ settings.py,
│  ├─ static,
│  │  └─ docs,
│  │     ├─ redoc.standalone.js,
│  │     ├─ swagger-ui-bundle.js,
│  │     └─ swagger-ui.css,
│  ├─ tests,
│  │  ├─ __init__.py,
│  │  ├─ test_dummy.py,
│  │  ├─ test_echo.py,
│  │  ├─ test_fastapi_movie_app.py,
│  │  ├─ test_rabbit.py,
│  │  └─ test_redis.py,
│  └─ web,
│     ├─ __init__.py,
│     ├─ api,
│     │  ├─ __init__.py,
│     │  ├─ docs,
│     │  │  ├─ __init__.py,
│     │  │  └─ views.py,
│     │  ├─ dummy,
│     │  │  ├─ __init__.py,
│     │  │  ├─ schema.py,
│     │  │  └─ views.py,
│     │  ├─ echo,
│     │  │  ├─ __init__.py,
│     │  │  ├─ schema.py,
│     │  │  └─ views.py,
│     │  ├─ monitoring,
│     │  │  ├─ __init__.py,
│     │  │  └─ views.py,
│     │  ├─ rabbit,
│     │  │  ├─ __init__.py,
│     │  │  ├─ schema.py,
│     │  │  └─ views.py,
│     │  ├─ redis,
│     │  │  ├─ __init__.py,
│     │  │  ├─ schema.py,
│     │  │  └─ views.py,
│     │  └─ router.py,
│     ├─ application.py,
│     └─ lifetime.py,
├─ poetry.lock,
└─ pyproject.toml,

```
