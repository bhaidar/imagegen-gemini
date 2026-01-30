#!/usr/bin/env python3
"""Generate images using Google Gemini API (Nano Banana models)."""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", "google-genai"])
    from google import genai
    from google.genai import types

MODELS = {
    "flash": "gemini-2.5-flash-preview-05-20",
    "flash-image": "gemini-2.5-flash-image",
    "pro-image": "gemini-3-pro-image-preview",
}


def generate_image(prompt: str, output_path: str = "generated_image.png", 
                   model: str = "flash", input_image: str = None) -> dict:
    """Generate an image from text, optionally editing an input image."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"success": False, "error": "GEMINI_API_KEY env var required. Get key: https://aistudio.google.com/apikey"}
    
    try:
        client = genai.Client(api_key=api_key)
        model_id = MODELS.get(model, MODELS["flash"])
        contents = []
        
        if input_image:
            path = Path(input_image)
            if not path.exists():
                return {"success": False, "error": f"Input image not found: {input_image}"}
            mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", 
                    "gif": "image/gif", "webp": "image/webp"}.get(path.suffix.lower().lstrip("."), "image/png")
            with open(path, "rb") as f:
                contents.append(types.Part.from_bytes(data=f.read(), mime_type=mime))
        
        contents.append(prompt)
        
        response = client.models.generate_content(
            model=model_id,
            contents=contents,
            config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
        )
        
        if response.candidates:
            for part in response.candidates[0].content.parts:
                if hasattr(part, "inline_data") and part.inline_data:
                    out = Path(output_path)
                    out.parent.mkdir(parents=True, exist_ok=True)
                    out.write_bytes(part.inline_data.data)
                    return {"success": True, "path": str(out.absolute()), "model": model_id}
        
        return {"success": False, "error": f"No image generated. Response: {response.text[:200] if response.text else 'empty'}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Generate images with Gemini API")
    parser.add_argument("prompt", help="Image description")
    parser.add_argument("-o", "--output", default="generated_image.png", help="Output path")
    parser.add_argument("-m", "--model", choices=list(MODELS.keys()), default="flash", help="Model")
    parser.add_argument("-i", "--input-image", help="Input image for editing")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()
    
    result = generate_image(args.prompt, args.output, args.model, args.input_image)
    
    if args.json:
        print(json.dumps(result, indent=2))
    elif result["success"]:
        print(f"Saved: {result['path']}")
    else:
        print(f"Error: {result['error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
