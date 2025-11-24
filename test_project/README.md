## Test project for pyminify

This is a project to test `pyminify` tool. Run `build.py` to minify the source code, and then run `fastapi dev --app app.app:app` to test the minified code.
The entrypoint is `app.app:app`.

The minified code SHOULD be able to run without any dependency (except dev deps).
Run `uv sync --only-dev` to install only dev dependencies, and run `fastapi dev --app app.app:app` to start the server.

### Endpoints
- `/`: SHOULD return `{"success": "Hello, world!"}`
- `/v0`: SHOULD return `{"version": "0"}`
- `/v0/router`: SHOULD return `{"message": "Hello from utils!"}`
