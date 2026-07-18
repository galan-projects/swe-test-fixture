# swe-test-fixture

Fixture repo for the v2.0 SWE agent capability tests. DO NOT use for real work.

## Layout

- `calculator/` — a tiny Python package
- `tests/` — pytest tests (some intentionally failing; see issue #2)
- `.github/workflows/ci.yml` — runs pytest on PRs

## Known bugs (intentional)

- Issue #2: `calculator.add()` returns the product instead of the sum.
