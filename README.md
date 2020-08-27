# ansible-server

A lightweight web interface for Ansible

## Setup

```
pip3 install uvicorn fastapi aiofiles umongo
```

## Running

For now i use Uvicorn to serve the ASGI app, but will probably switch to Hypercorn as it's support H3/QUIC protocols

```
python3 run.py
```
