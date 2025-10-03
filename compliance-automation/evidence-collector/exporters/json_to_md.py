#!/usr/bin/env python3
import os, json, sys, hashlib, datetime

SRC = "compliance-automation/reports/json"
DST = "compliance-automation/evidence-store/obsidian"

def sha1(path):
    h = hashlib.sha1()
    with open(path,'rb') as f:
        while True:
            b = f.read(8192)
            if not b: break
            h.update(b)
    return h.hexdigest()

def main():
    today = datetime.date.today().isoformat()
    md_path = os.path.join(DST, f"scan-summary-{today}.md")
    with open(md_path, "w") as md:
        md.write(f"# Compliance Scan Summary — {today}\n\n")
        for root, _, files in os.walk(os.path.join(SRC, today)):
            for fn in files:
                p = os.path.join(root, fn)
                try:
                    data = None
                    if fn.endswith(".json"):
                        with open(p) as f:
                            try:
                                data = json.load(f)
                            except Exception:
                                data = None
                    md.write(f"## {fn}\n\n")
                    md.write(f"- Path: `{p}`\n")
                    md.write(f"- SHA1: `{sha1(p)}`\n")
                    if data and isinstance(data, dict):
                        # try common keys
                        fails = data.get("fail", data.get("Failed", data.get("failures")))
                        passes = data.get("pass", data.get("Passed", data.get("passes")))
                        if fails is not None or passes is not None:
                            md.write(f"- Pass: **{passes}** | Fail: **{fails}**\n")
                    md.write("\n")
        print(f"Wrote: {md_path}")

if __name__ == "__main__":
    os.makedirs(os.path.join(SRC, today:=datetime.date.today().isoformat()), exist_ok=True)
    os.makedirs(DST, exist_ok=True)
    main()
