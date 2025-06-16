#! /bin/bash

start() {
    source .venv/bin/activate
    cd ./src
    python3 server.py
}

exit() {
    deactivate
    trap - SIGINT SIGTERM
    kill 0
}

(trap 'exit' SIGINT SIGTERM; start)