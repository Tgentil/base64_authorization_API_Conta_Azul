""" Esse script gerar uma autorização no formato "Basic" em um hash em Base64 utilizando clientID e um secretID """

import base64

CLIENT_ID = "seu_client_id"
CLIENT_SECRET = "seu_client_secret"

credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
base64_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

print(f"Authorization: Basic {base64_credentials}")
