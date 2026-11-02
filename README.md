# Streaming percentiles

Calculate p50, p95, and p99 directly from a continuous stream of numbers. We keep this completely dependency-free to avoid bloating your environment.

The Python Histogram implementation relies strictly on the standard library. You do not need to install any external services or third-party packages.

```
percentile.py
```
Check the Python Histogram test file alongside the main implementation to see concrete usage examples.

## FAQ

**Do I need anything besides `INFRAI_API_KEY`?**  
Just `python3` and your API key. `percentile.py` handles the actual HTTPS request under the hood. This means you skip installing an SDK or dealing with version sync issues. For a simple histogram utility, that keeps the dependency tree perfectly clean and your cold starts fast.

**How much of this is reusable?**  
You really only need to copy `percentile.py`. The rest of the code is just scaffolding to make the example execute as a standalone script.