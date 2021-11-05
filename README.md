# Cog Markdown example

<a href="https://replicate.ai/andreasjansson/cog-markdown-example"><img src="https://img.shields.io/static/v1?label=Replicate&message=Demo and Docker Image&color=darkgreen" height=20></a>

This is a simple example to demonstrate how to output markdown from Cog.

If Cog returns a `pathlib.Path` pointing to a generated markdown file with extension `.md` it will be rendered to HTML on Replicate. This is demonstrated in the `predict()` function in predict.py.

We use [GitHub-flavored Markdown](https://github.github.com/gfm) to do the rendering, but there may be some features missing for security reasons.
