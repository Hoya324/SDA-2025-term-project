"""Matplotlib helpers to render Korean labels without glyph issues.

Usage (top of each notebook cell before plotting):
    from plot_config import use_korean_font
    use_korean_font()
"""

from matplotlib import font_manager as fm
from matplotlib.ft2font import FT2Font
import matplotlib.pyplot as plt
from pathlib import Path


def _has_korean_glyph(font_path, sample="가"):
    """Check if the font file supports the given Korean glyph."""
    try:
        ft = FT2Font(font_path)
        return ft.get_char_index(ord(sample)) != 0
    except Exception:
        return False


def _register_local_fonts():
    """Register locally installed Nanum fonts explicitly (Homebrew installs to ~/Library/Fonts)."""
    candidates = [
        "/Users/hoyana/Library/Fonts/NanumGothic-Regular.ttf",
        "/Users/hoyana/Library/Fonts/NanumGothic-Bold.ttf",
        "/Users/hoyana/Library/Fonts/NanumGothic-ExtraBold.ttf",
        "/Library/Fonts/NanumGothic-Regular.ttf",
        "/Library/Fonts/NanumGothic-Bold.ttf",
        "/Library/Fonts/NanumGothic-ExtraBold.ttf",
    ]
    registered = []
    for path in candidates:
        p = Path(path)
        if not p.exists():
            continue
        try:
            fm.fontManager.addfont(str(p))
            name = fm.FontProperties(fname=str(p)).get_name()
            registered.append((name, str(p)))
        except Exception:
            continue
    return registered


def _pick_font(candidates=None):
    """Return the first available font that has Korean glyphs."""
    registered = _register_local_fonts()
    # Pull names from any registered fonts to the front of the list.
    registered_names = [name for name, _ in registered]
    if candidates is None:
        candidates = (
            *registered_names,
            "NanumGothic",
            "Malgun Gothic",
            "AppleGothic",
            "Noto Sans CJK KR",
            "DejaVu Sans",
        )
    for font in candidates:
        try:
            path = fm.findfont(font, fallback_to_default=False)
            if _has_korean_glyph(path):
                return font, path
        except Exception:
            continue
    # Final fallback
    try:
        path = fm.findfont("DejaVu Sans")
    except Exception:
        path = ""
    return "DejaVu Sans", path


def use_korean_font():
    """Configure matplotlib to use a Korean-capable font and fix minus signs."""
    registered = _register_local_fonts()
    # Rebuild font cache so newly installed fonts (e.g., NanumGothic) are visible.
    try:
        fm._rebuild()
    except Exception:
        pass

    font, path = _pick_font()
    plt.rcParams["font.family"] = [
        font,  # best match
        "NanumGothic",  # explicit request after installation
        "Malgun Gothic",
        "AppleGothic",
        "Noto Sans CJK KR",
        "DejaVu Sans",
    ]
    plt.rcParams["axes.unicode_minus"] = False
    # Optional: show which font is active so plots are reproducible.
    print(f"[plot_config] Matplotlib font set to: {font} ({path})")
    if registered:
        joined = ", ".join(f"{name} -> {p}" for name, p in registered)
        print(f"[plot_config] Registered local fonts: {joined}")
    return font
