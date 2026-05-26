"""Add graph_title, indicator_name, and graph_titles to all meta YAML files."""
import os
import re

META_DIR = os.path.join(os.path.dirname(__file__), '..', 'meta')

for filename in sorted(os.listdir(META_DIR)):
    if not filename.endswith('.yml'):
        continue

    indicator_id = filename[:-4]  # e.g. "1-10"
    parts = indicator_id.split('-')
    if len(parts) != 2:
        continue

    goal, code = parts
    series_key = f"sdg_{int(goal):02d}_{code}"  # e.g. "sdg_01_10"

    filepath = os.path.join(META_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'graph_titles' in content:
        print(f"SKIP {filename} (already has graph_titles)")
        continue

    addition = (
        f"\ngraph_title: global_indicators.{indicator_id}-title\n"
        f"indicator_name: global_indicators.{indicator_id}-title\n"
        f"graph_titles:\n"
        f"- series: SERIES.{series_key}\n"
        f"  title: SERIES.{series_key}\n"
    )

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(addition)

    print(f"OK  {filename} -> SERIES.{series_key}")
