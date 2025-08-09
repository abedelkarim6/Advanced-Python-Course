Alright — here’s the **student-friendly homework sheet** version.
It’s written as if you’re talking directly to them, guiding step-by-step.

---

## **Homework: Absolute & Relative Imports in Python**

Hey Python pros-in-training 👋 —
You’ve been writing functions and classes for a while, but now it’s time to level up your **project organization** skills.
Today we’ll practice **absolute imports first**, then move into **relative imports** so you understand both.

---

### **📂 Step 1 — Your Starting Project (Absolute Imports)**

Here’s your starting folder structure. Create it exactly like this:

```
my_project/
│
├── main.py
│
├── utils/
│   ├── math_utils.py
│   └── string_utils.py
│
└── features/
    ├── feature1.py
    └── feature2.py
```

**Important:**
No `__init__.py` files yet — we’ll add them later.

---

### **💡 Step 2 — Absolute Imports Practice**

Absolute imports mean we **start from the top-level folder** when importing.

1. Inside `math_utils.py`, write:

```python
def add_numbers(a, b):
    return a + b
```

2. Inside `string_utils.py`, write:

```python
def reverse_text(text):
    return text[::-1]
```

3. Inside `main.py`, import and use them:

```python
from utils.math_utils import add_numbers
from utils.string_utils import reverse_text

print(add_numbers(5, 7))
print(reverse_text("Python"))
```

4. Run:

```bash
python main.py
```

✅ You should see:

```
12
nohtyP
```

---

### **🚀 Step 3 — Adding a New Feature (Still Absolute Imports)**

Inside `features/feature1.py`, write:

```python
from utils.math_utils import add_numbers

def feature1_demo():
    print("Feature 1 result:", add_numbers(10, 20))
```

Now update `main.py`:

```python
from features.feature1 import feature1_demo

feature1_demo()
```

Run again — it should print the feature result.

---

### **🔄 Step 4 — Switching to Relative Imports**

Now, let’s make the folders **real Python packages** by adding `__init__.py` files.

Your structure should now be:

```
my_project/
│
├── __init__.py
├── main.py
│
├── utils/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
│
└── features/
    ├── __init__.py
    ├── feature1.py
    └── feature2.py
```

---

### **📦 Step 5 — Changing to Relative Imports**

In `features/feature1.py`, replace:

```python
from utils.math_utils import add_numbers
```

with:

```python
from ..utils.math_utils import add_numbers
```

We’re now saying:
“Go **up one folder** (`..`) from `features`, then into `utils` and import `math_utils`.”

---

### **🎯 Step 6 — Bonus Challenge**

1. Create `feature2.py` that uses both:

   * `add_numbers()` from `math_utils`
   * `reverse_text()` from `string_utils`
     Use **relative imports** for both.
2. Try running:

```bash
python -m my_project.main
```

Notice how **relative imports work here**, but may fail if you run `python main.py` directly.
Think about why that happens. (Hint: it’s about where Python thinks your “top-level” is.)

---

### **🏆 What You’ll Learn**

* How to structure a multi-file Python project.
* The difference between **absolute** and **relative** imports.
* Why `__init__.py` matters for packages.
* How to run modules with `python -m`.


