# Flappy-Bird-Python

A tiny, dependency-free (apart from Pygame) re-creation of the classic Flappy Bird.  
Perfect for learning how to structure a simple 2-D game loop in Python.

## Quick start

```bash
# 1. Clone
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>

# 2. (Optional) create & activate virtual-env
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install deps
pip install -r requirements.txt

# 4. Run
python -m src.main
```

## Controls

* **Space / ↑ / Click** – flap
* **Esc** – quit

## Folder layout

| Path              | Purpose                                 |
| ----------------- | --------------------------------------- |
| `src/settings.py` | All tunable constants (window, speeds…) |
| `src/bird.py`     | Bird sprite + physics                   |
| `src/pipe.py`     | Pipe pair logic                         |
| `src/main.py`     | Game loop & collision detection         |

MIT licensed – hack away!
