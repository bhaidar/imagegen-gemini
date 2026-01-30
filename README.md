# Gemini Image Generation Skill for Claude Code

Generate and edit images using Google's Gemini API with Nano Banana models.

## Features

- **Text to Image**: Generate images from text prompts
- **Image Editing**: Modify existing images with text instructions
- **Multiple Models**: Choose between speed and quality
- **Claude Code Integration**: Works seamlessly as a Claude Code skill

## Requirements

- Python 3.9+
- Google Gemini API key (free tier available)

## Installation

### For Claude Code (CLI)

**Global install** (available in all projects):
```bash
git clone https://github.com/yourusername/imagegen-gemini.git ~/.claude/skills/imagegen-gemini
```

**Project install** (available in current project only):
```bash
git clone https://github.com/yourusername/imagegen-gemini.git .claude/skills/imagegen-gemini
```

### For Claude.ai (Web/App)

1. Download this repo as a ZIP
2. Go to Settings > Capabilities > Skills
3. Click "Upload skill" and select the ZIP file

### API Key Setup

Get your free API key at: https://aistudio.google.com/apikey

**For Claude Code**, add to your shell profile (`~/.bashrc` or `~/.zshrc`):
```bash
export GEMINI_API_KEY="your_api_key_here"
```

**For Claude.ai**, the skill will prompt you if the key is missing.

### Standalone Usage

```bash
git clone https://github.com/yourusername/imagegen-gemini.git
cd imagegen-gemini
pip install -r requirements.txt
export GEMINI_API_KEY="your_api_key_here"
```

## Usage

### Basic Image Generation

```bash
python scripts/generate_image.py "A majestic mountain landscape at golden hour" -o landscape.png
```

### Edit an Existing Image

```bash
python scripts/generate_image.py "Add dramatic storm clouds to the sky" -i photo.jpg -o edited.png
```

### Choose a Model

```bash
# Fast generation (default)
python scripts/generate_image.py "A cute robot" -m flash -o robot.png

# Speed optimized (Nano Banana)
python scripts/generate_image.py "A cute robot" -m flash-image -o robot.png

# Highest quality (Nano Banana Pro with thinking)
python scripts/generate_image.py "A cute robot" -m pro-image -o robot.png
```

### JSON Output

```bash
python scripts/generate_image.py "A sunset" -o sunset.png --json
```

Output:
```json
{
  "success": true,
  "path": "/absolute/path/to/sunset.png",
  "model": "gemini-2.5-flash-preview-05-20"
}
```

## Available Models

| Model | Gemini ID | Description |
|-------|-----------|-------------|
| `flash` | gemini-2.5-flash-preview-05-20 | Fast, general purpose (default) |
| `flash-image` | gemini-2.5-flash-image | Nano Banana, optimized for speed |
| `pro-image` | gemini-3-pro-image-preview | Nano Banana Pro, highest quality |

## Command Reference

```
python scripts/generate_image.py <prompt> [options]

Arguments:
  prompt                Text description of the image to generate

Options:
  -o, --output PATH     Output file path (default: generated_image.png)
  -m, --model MODEL     Model to use: flash, flash-image, pro-image
  -i, --input-image     Input image path for editing
  --json                Output result as JSON
  -h, --help            Show help message
```

## Prompting Tips

### Be Descriptive
Include subject, style, lighting, mood, and composition details.

```
"A serene Japanese garden with a koi pond, soft morning light filtering through maple trees, 
watercolor painting style, peaceful atmosphere"
```

### Specify Style
Add style keywords to guide the output.

```
"A portrait of an astronaut, oil painting style, dramatic chiaroscuro lighting"
"A city skyline, minimalist vector art, limited color palette"
"A forest scene, Studio Ghibli style, warm autumn colors"
```

### For Text in Images
Keep text under 25 characters for best results.

```
"A coffee shop sign that says 'OPEN', neon lights, night scene"
```

## Programmatic Usage

```python
import sys
sys.path.insert(0, '/path/to/imagegen-gemini')
from scripts.generate_image import generate_image

result = generate_image(
    prompt="A cyberpunk city with neon lights",
    output_path="cyberpunk.png",
    model="flash-image"
)

if result["success"]:
    print(f"Image saved to: {result['path']}")
else:
    print(f"Error: {result['error']}")
```

## Troubleshooting

### "GEMINI_API_KEY environment variable is required"
Set your API key:
```bash
export GEMINI_API_KEY="your_key_here"
```

### "No image generated"
Some prompts may be blocked by safety filters. Try rephrasing your prompt.

### Rate Limits
The free tier has usage limits. Check https://ai.google.dev/pricing for current limits.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Links

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Get API Key](https://aistudio.google.com/apikey)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
