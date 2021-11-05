import tempfile
from pathlib import Path

import cog


class Predictor(cog.Predictor):
    def setup(self):
        pass

    @cog.input("italic_text", type=str, help="Text that will be rendered as italic")
    @cog.input("table_text", type=str, help="Text that will go into every table cell")
    def predict(self, italic_text, table_text):
        out = f"""# Markdown Cog example

This is an example of producing Markdown from Cog.

## Italic text

_{italic_text}_

## A table

| First column | Second column | Third column
| --- | --- | --- |
| {table_text} | {table_text} | {table_text}
| {table_text} | {table_text} | {table_text}
| {table_text} | {table_text} | {table_text}
| {table_text} | {table_text} | {table_text}
"""
        out_path = Path(tempfile.mkdtemp()) / "out.md"
        with open(out_path, "w") as f:
            f.write(out)
        return out_path
