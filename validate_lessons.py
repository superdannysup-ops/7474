"""Offline lesson and metadata validation; does not require Minecraft or Gradle."""
import json
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parents[1]
resources = root / "src" / "main" / "resources"
words = json.loads((resources / "data/hangulcraft/vocabulary.json").read_text("utf-8"))
grammar = json.loads((resources / "data/hangulcraft/grammar.json").read_text("utf-8"))
mod = json.loads((resources / "fabric.mod.json").read_text("utf-8"))
assert mod["id"] == "hangulcraft"
assert len(words) >= 100 and len(grammar) >= 15
required = {"id", "ko", "en", "pronunciation", "example_ko", "example_en", "level", "category", "triggers"}
ids = Counter(w["id"] for w in words)
assert max(ids.values()) == 1, f"Duplicate word ids: {ids}"
triggers = Counter((w["category"] == "mobs", t) for w in words for t in w["triggers"])
assert max(triggers.values()) == 1, f"Duplicate triggers: {[(k,v) for k,v in triggers.items() if v>1]}"
for w in words:
    assert required <= w.keys(), w
    assert w["level"] in {"A1", "A2"}, w
    assert all(w[k].strip() for k in ("ko", "en", "pronunciation", "example_ko", "example_en")), w
    assert all(t.startswith("minecraft:") for t in w["triggers"]), w
for g in grammar:
    assert {"id", "prompt", "answers", "correct", "explanation", "level"} <= g.keys(), g
    assert len(g["answers"]) == len(set(g["answers"])) == 4, g
    assert 0 <= g["correct"] < 4, g
    assert g["level"] in {"A1", "A2"}, g
assert len(set(g["id"] for g in grammar)) == len(grammar)
print(f"PASS: {len(words)} vocabulary entries, {len(grammar)} grammar questions, {len(triggers)} unique trigger mappings")
