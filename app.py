from flask import Flask, jsonify
import os
import logging
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME")
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"

credential = ManagedIdentityCredential()
client = SecretClient(vault_url=KV_URI, credential=credential)

@app.route("/")
def home():
    secret = client.get_secret("api-message").value
    app.logger.info("Read secret from Key Vault")
    return f"✅ {secret}"


@app.route("/health")
def health():
    return jsonify(status="OK")



if __name__ == "__main__":
    app.run()

