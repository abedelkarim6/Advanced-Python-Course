1. We always include `__init__.py` files to enable relative import.
2. We always call the `utils.py` from the `main.py`
3. We never run the utils alone while it includes relative import.
4. When utils include relative import, and we want to test it alone --> we add the `sys.append()` before the relative import
