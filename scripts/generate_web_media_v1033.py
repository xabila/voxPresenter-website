#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates all v1.0.33 localized web visual & video assets for voxpresenter.com:
1. Updated 2x Retina WebP prompter/live-stage captures:
   - assets/screenshot-prompter-{fr,en,es,de,pt}.webp (560x1218)
   - assets/screenshot-prompter.png & screenshot-prompter_EN.PNG fallbacks
2. Localized 1200x630 OpenGraph / X / iMessage / LinkedIn social preview cards:
   - assets/og-card-{fr,en,es,de,pt}.jpg (1200x630, crisp < 130 KB)
3. Optimized 5-locale web showcase videos (zero-LCP-impact lazy streaming):
   - assets/videos/preview-{fr,en,es,de,pt}.mp4  (554x1200 H.264 +faststart, ~850 KB)
   - assets/videos/preview-{fr,en,es,de,pt}.webm (554x1200 VP9, ~650 KB)
   - assets/videos/poster-preview-{fr,en,es,de,pt}.webp (554x1200 WebP poster, ~32 KB)
"""

import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw

REPO_ROOT = Path("/Users/xabi/DEV/EyePrompteur")
SITE_ROOT = REPO_ROOT / "site-web"
ASSETS_DIR = SITE_ROOT / "assets"
VIDEOS_OUT_DIR = ASSETS_DIR / "videos"
SRC_VIDEOS_DIR = REPO_ROOT / "Tools" / "template-appstore-video" / "out"
SCRATCH_CAPTURES = Path("/Users/xabi/.gemini/antigravity/brain/95b1f77e-d59b-4cbd-8bb7-08af4a28982f/scratch/v22_source_captures")
WATCH_DIR = REPO_ROOT / ".asc" / "screenshots" / "watch"

sys.path.insert(0, str(REPO_ROOT / "Marketing"))
from generate_in_app_event_v24 import (
    STAGE_LOCALES,
    FONT_SANS,
    FONT_ROUNDED,
    load_font,
    wrap_text_lines,
    render_live_stage_screen,
    make_editorial_cream_canvas,
    render_iphone_titanium,
    render_watch_titanium,
    rounded_mask,
)

OG_COPY = {
    "fr": {
        "kicker": "IPHONE · IPAD · APPLE WATCH · MAC & PC",
        "headline": "Parlez, filmez en 4K et pilotez la scène.",
        "sub": "Suivi vocal 100 % hors-ligne, Studio Caméra 4K MP4, signets live & clicker.",
        "pills": ["Voix hors-ligne", "Caméra 4K MP4", "Scène & Watch"],
    },
    "en": {
        "kicker": "IPHONE · IPAD · APPLE WATCH · MAC & PC",
        "headline": "Speak, shoot in 4K, and command the stage.",
        "sub": "100% offline voice tracking, 4K MP4 Camera Studio, live cues & clicker.",
        "pills": ["Offline Voice", "4K MP4 Studio", "Stage & Watch"],
    },
    "es": {
        "kicker": "IPHONE · IPAD · APPLE WATCH · MAC Y PC",
        "headline": "Habla, graba en 4K y domina el escenario.",
        "sub": "Voz 100 % sin conexión, Estudio Cámara 4K MP4, marcadores y mando.",
        "pills": ["Voz offline", "Cámara 4K MP4", "Escena y Watch"],
    },
    "de": {
        "kicker": "IPHONE · IPAD · APPLE WATCH · MAC & PC",
        "headline": "Sprechen, in 4K filmen & die Bühne steuern.",
        "sub": "100 % lokale Spracherkennung, 4K-Kamerastudio, Live-Marken & Clicker.",
        "pills": ["100 % Offline", "4K-Kamerastudio", "Bühne & Watch"],
    },
    "pt": {
        "kicker": "IPHONE · IPAD · APPLE WATCH · MAC E PC",
        "headline": "Fale, grave em 4K e comande o palco.",
        "sub": "Voz 100% offline, Estúdio Câmera 4K MP4, favoritos ao vivo e passador.",
        "pills": ["Voz offline", "Câmera 4K MP4", "Palco e Watch"],
    },
}


def build_og_card_1200x630(lang: str, cam_scr: Image.Image, stage_scr: Image.Image, watch_scr: Image.Image) -> Image.Image:
    W, H = 1200, 630
    bg = make_editorial_cream_canvas(W, H, aura_cy_ratio=0.46)
    d = ImageDraw.Draw(bg)
    cp = OG_COPY[lang]

    # Right-side 3-device hardware showcase (cleanly framed with generous right margin)
    cam_art = render_iphone_titanium(cam_scr, target_w=240).rotate(4.0, resample=Image.Resampling.BICUBIC, expand=True)
    stage_art = render_iphone_titanium(stage_scr, target_w=244).rotate(-3.2, resample=Image.Resampling.BICUBIC, expand=True)
    watch_art = render_watch_titanium(watch_scr, case_w=154).rotate(-4.5, resample=Image.Resampling.BICUBIC, expand=True)

    bg.alpha_composite(cam_art, (518, 12))
    bg.alpha_composite(stage_art, (752, 26))
    bg.alpha_composite(watch_art, (922, 268))

    # Left-side editorial brand lockup + headline + pills (x = 58 .. 560)
    icon_img = Image.open(ASSETS_DIR / "icon.png").convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS)
    icon_mask = rounded_mask((64, 64), 15)
    bg.paste(icon_img, (60, 56), icon_mask)

    f_brand = load_font(FONT_ROUNDED, 34, 800)
    f_kicker = load_font(FONT_SANS, 17, 800)
    f_head = load_font(FONT_ROUNDED, 48, 820)
    f_sub = load_font(FONT_SANS, 23, 520)
    f_pill = load_font(FONT_SANS, 18, 720)

    d.text((138, 69), "VoxPresenter", font=f_brand, fill=(155, 47, 32, 255))
    # Star rating badge next to brand
    d.rounded_rectangle((386, 69, 490, 107), radius=19, fill=(245, 227, 223, 255), outline=(181, 59, 43, 90), width=1)
    d.text((403, 77), "★ 4.9", font=f_pill, fill=(155, 47, 32, 255))

    # Kicker
    d.text((60, 150), cp["kicker"], font=f_kicker, fill=(155, 47, 32, 255))

    # Headline (max width 490px)
    h_lines = wrap_text_lines(d, cp["headline"], f_head, 495)
    hy = 186
    for hl in h_lines[:3]:
        d.text((60, hy), hl, font=f_head, fill=(26, 20, 16, 255))
        hy += 56

    # Subtitle
    s_lines = wrap_text_lines(d, cp["sub"], f_sub, 490)
    sy = hy + 18
    for sl in s_lines[:3]:
        d.text((60, sy), sl, font=f_sub, fill=(78, 68, 59, 255))
        sy += 32

    # Bottom pills
    px = 60
    py = H - 96
    for pill_txt in cp["pills"]:
        bb = d.textbbox((0, 0), pill_txt, font=f_pill)
        pw = (bb[2] - bb[0]) + 34
        d.rounded_rectangle((px, py, px + pw, py + 42), radius=21, fill=(19, 14, 9, 255))
        d.text((px + 17, py + 10), pill_txt, font=f_pill, fill=(247, 242, 233, 255))
        px += pw + 10

    return bg.convert("RGB")


def encode_web_videos() -> None:
    VIDEOS_OUT_DIR.mkdir(parents=True, exist_ok=True)
    for cfg in STAGE_LOCALES:
        short = cfg["short"]
        upper = short.upper()
        src_mp4 = SRC_VIDEOS_DIR / f"VoxPresenter-Preview-{upper}.mp4"
        if not src_mp4.exists():
            raise FileNotFoundError(f"Missing source video: {src_mp4}")

        out_mp4 = VIDEOS_OUT_DIR / f"preview-{short}.mp4"
        out_webm = VIDEOS_OUT_DIR / f"preview-{short}.webm"
        out_poster = VIDEOS_OUT_DIR / f"poster-preview-{short}.webp"

        # 1. Extract sharp poster frame at t=7.2s (4K Camera Studio / active highlight beat) -> 554x1200 WebP
        subprocess.run(
            [
                "ffmpeg", "-y", "-ss", "7.2", "-i", str(src_mp4),
                "-frames:v", "1", "-vf", "scale=554:1200:flags=lanczos",
                "-c:v", "libwebp", "-quality", "82", str(out_poster),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # 2. Encode faststart H.264 MP4 (554x1200, 24fps, muted -an, CRF 27 -> ~750-950 KB for 24s!)
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(src_mp4),
                "-an",
                "-vf", "scale=554:1200:flags=lanczos,fps=24",
                "-c:v", "libx264", "-preset", "slow", "-crf", "27",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                str(out_mp4),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # 3. Encode VP9 WebM (554x1200, 24fps, muted -an, CRF 34 -> ~550-750 KB for 24s!)
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(src_mp4),
                "-an",
                "-vf", "scale=554:1200:flags=lanczos,fps=24",
                "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "34",
                "-row-mt", "1", "-deadline", "good", "-cpu-used", "2",
                str(out_webm),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(
            f"✓ [{short}] Video encoded: MP4={out_mp4.stat().st_size // 1024}KB | "
            f"WebM={out_webm.stat().st_size // 1024}KB | Poster={out_poster.stat().st_size // 1024}KB"
        )


def main() -> None:
    for cfg in STAGE_LOCALES:
        short = cfg["short"]
        asc_loc = cfg["asc"]

        cam_scr = Image.open(SCRATCH_CAPTURES / short / "iphone_cam4k.png").convert("RGBA")
        stage_scr = render_live_stage_screen(cfg)
        watch_scr = Image.open(WATCH_DIR / asc_loc / "02_watch_dual_deck.png").convert("RGBA")

        # 1. Save 2x Retina Live Stage prompter screenshot (560x1218 WebP)
        stage_560 = stage_scr.convert("RGB").resize((560, 1218), Image.Resampling.LANCZOS)
        webp_path = ASSETS_DIR / f"screenshot-prompter-{short}.webp"
        stage_560.save(webp_path, format="WEBP", quality=84, method=6)

        if short == "fr":
            stage_560.save(ASSETS_DIR / "screenshot-prompter.png", format="PNG", optimize=True)
        elif short == "en":
            stage_560.save(ASSETS_DIR / "screenshot-prompter_EN.PNG", format="PNG", optimize=True)

        # 2. Save 1200x630 localized OpenGraph card (JPEG quality=88 + WebP)
        og_img = build_og_card_1200x630(short, cam_scr, stage_scr, watch_scr)
        og_jpg = ASSETS_DIR / f"og-card-{short}.jpg"
        og_webp = ASSETS_DIR / f"og-card-{short}.webp"
        og_img.save(og_jpg, format="JPEG", quality=88, optimize=True, progressive=True)
        og_img.save(og_webp, format="WEBP", quality=84, method=6)

        print(
            f"✓ [{short}] Saved {webp_path.name} ({webp_path.stat().st_size // 1024}KB) & "
            f"{og_jpg.name} ({og_jpg.stat().st_size // 1024}KB)"
        )

    if "--cards-only" not in sys.argv:
        encode_web_videos()


if __name__ == "__main__":
    main()
