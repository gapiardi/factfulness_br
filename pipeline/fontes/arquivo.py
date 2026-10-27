"""Download de arquivos oficiais, registrando URL, data e hash num manifesto para auditoria."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

TIMEOUT = 120


def baixar(url: str, destino: Path) -> dict:
    destino.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    destino.write_bytes(resp.content)

    registro = {
        "url": url,
        "arquivo": destino.name,
        "sha256": hashlib.sha256(resp.content).hexdigest(),
        "bytes": len(resp.content),
        "baixado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    _atualizar_manifesto(destino.parent / "manifesto.json", registro)
    return registro


def _atualizar_manifesto(caminho: Path, registro: dict) -> None:
    manifesto = json.loads(caminho.read_text(encoding="utf-8")) if caminho.exists() else []
    anterior = next((r for r in manifesto if r["arquivo"] == registro["arquivo"]), None)
    # Fonte oficial pode ser revisada sem aviso; hash diferente exige reconferência.
    if anterior and anterior["sha256"] != registro["sha256"]:
        print(f"ATENÇÃO: {registro['arquivo']} mudou desde {anterior['baixado_em']}. Reconferir valores.")

    manifesto = [r for r in manifesto if r["arquivo"] != registro["arquivo"]] + [registro]
    caminho.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
