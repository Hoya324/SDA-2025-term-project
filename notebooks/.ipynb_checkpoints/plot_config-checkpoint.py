"""Matplotlib helpers to render Korean labels without glyph issues.

Usage (top of each notebook cell before plotting):
    from plot_config import use_korean_font
    use_korean_font()
"""

from matplotlib import font_manager as fm
import matplotlib.pyplot as plt


def _pick_font(candidates=None):
    """Return the first available font from candidates."""
    if candidates is None:
        candidates = ("AppleGothic", "NanumGothic", "Malgun Gothic", "DejaVu Sans")
    for font in candidates:
        try:
            fm.findfont(font, fallback_to_default=False)
            return font
        except Exception:
            continue
    return "DejaVu Sans"


def use_korean_font():
    """Configure matplotlib to use a Korean-capable font and fix minus signs."""
    font = _pick_font()
    plt.rcParams["font.family"] = font
    plt.rcParams["axes.unicode_minus"] = False
    # Optional: show which font is active so plots are reproducible.
    print(f"[plot_config] Matplotlib font set to: {font}")
    return font
