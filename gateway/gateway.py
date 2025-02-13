#!/bin/env python
"""
    Grid Gateway is a Flask based application used to manage / monitor / control and route grid workers remotely.
"""
import os
import sys

import argparse

from app import create_app

parser = argparse.ArgumentParser(description="Run Grid Gatway application.")


parser.add_argument(
    "--port",
    "-p",
    type=int,
    help="Port number of the socket.io server, e.g. --port=8777. Default is os.environ.get('GRID_GATEWAY_PORT', None).",
    default=os.environ.get("GRID_GATEWAY_PORT", None),
)

parser.add_argument(
    "--host",
    type=str,
    help="Grid node host, e.g. --host=0.0.0.0. Default is os.environ.get('GRID_GATEWAY_HOST','0.0.0.0').",
    default=os.environ.get("GRID_GATEWAY_HOST", "0.0.0.0"),
)

parser.add_argument(
    "--num_replicas",
    type=int,
    help="Number of replicas to provide fault tolerance to model hosting. If None no replica is used (aka num_replicas = 1). Default is os.environ.get('NUM_REPLICAS', None).",
    default=os.environ.get("NUM_REPLICAS", None),
)


if __name__ == "__main__":
    args = parser.parse_args()
    app = create_app(debug=False, n_replica=args.num_replicas)
    app.run(host=args.host, port=args.port)
else:
    num_replicas = os.environ.get("N_REPLICAS", None)
    app = create_app(debug=False, n_replica=num_replicas)
