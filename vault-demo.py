from flask import Flask
import hvac
import os

app = Flask(__name__)

required_env_vars = ["VAULT_URL", "VAULT_TOKEN", "VAULT_PATH"]

def checkEnv(var):
    if not var in os.environ:
        app.logger.warning(f"Please set {var} in environment")

@app.route('/')
def main():
    for var in required_env_vars:
        checkEnv(var)

    try:
        vault_url = os.getenv("VAULT_URL")
        vault_token = os.getenv("VAULT_TOKEN")
        vault_path = os.getenv("VAULT_PATH")

        client = hvac.Client(url=vault_url,token=vault_token)
        app.logger.warning(f"Vault client is authenticated: {client.is_authenticated()}")
        read_response = client.secrets.kv.read_secret_version(path=vault_path)
        app.logger.warning(read_response["data"])
        return read_response["data"]
    except:
        return "Can not connect to Vault. Check logs."

if __name__ == '__main__':
    app.run(host='0.0.0.0')