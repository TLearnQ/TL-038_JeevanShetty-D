import json, logging, os

logging.basicConfig(filename="json_audit.log",
                    level=logging.INFO,
                    format="%(message)s")

def process_json(folder):
    ok = 0
    for fname in os.listdir(folder):
        if fname.endswith(".json"):
            try:
                with open(os.path.join(folder, fname)) as f:
                    json.load(f)
                logging.info(f"ok: {fname}")
                ok += 1
            except Exception as e:
                logging.info(f"error in {fname}: {e}")
    return f"valid={ok}"

print(process_json("configs"))