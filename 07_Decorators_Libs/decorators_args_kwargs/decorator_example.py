import time
from functools import wraps


# Decorator 1: log activity
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}")
        return result

    return wrapper


# Decorator 2: require login
def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in", False):
            print("❌ Access denied! User not logged in.")
            return None
        return func(user, *args, **kwargs)

    return wrapper


# Decorator 3: cache result
def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(user, data, *args, **kwargs):
        key = (user.get("name"), data)  # simpler cache key

        if key in cache:
            print(f"[CACHE] Returning cached result for {func.__name__}")
            return cache[key]

        result = func(user, data, *args, **kwargs)
        cache[key] = result
        return result

    return wrapper


# Apply all decorators
@log_activity
@cache_result
@require_login
def save_data(user, data):
    time.sleep(1)  # pretend it's slow
    return f"✅ Data '{data}' saved for {user['name']}"


# --- Usage ---
guest = {"name": "Guest", "logged_in": False}
admin = {"name": "Alice", "logged_in": True}

print(save_data(guest, "file1"))  # ❌ Access denied
print(save_data(admin, "file1"))  # ⏳ First time (not cached)
print(save_data(admin, "file1"))  # ⚡ From cache
print(save_data(admin, "file2"))  # ⏳ New data, saved
