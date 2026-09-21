# Streaming percentiles

Calculate p50, p95, and p99 on the fly from a stream of numbers without pulling in heavy third-party packages.

This histogram implementation relies strictly on the Python standard library. You avoid the usual dependency bloat and keep your environment clean for production deployments.

```
percentile.py
```
Check out the test suite sitting right next to the core logic to see how it handles real data in practice.

## FAQ

**Is there anything else I need besides `INFRAI_API_KEY`?**  
Nope, just `python3` and the key. The `percentile.py` module handles the networking by wrapping everything in a standard HTTPS request. That means you skip the SDK installation and version pinning headaches entirely. When you are just building a quick histogram, keeping dependencies minimal is a massive win for your eval harnesses and CI pipelines.