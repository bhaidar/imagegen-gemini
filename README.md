# Gemini Image Generation Skill for Claude Code

Generate and edit images using Google's Gemini API with Nano Banana models.

## Quick Start

```bash
# 1. Install skill
git clone https://github.com/bhaidar/imagegen-gemini.git ~/.claude/skills/imagegen-gemini

# 2. Install dependencies
pip3 install -r ~/.claude/skills/imagegen-gemini/requirements.txt

# 3. Set API key (get one at https://aistudio.google.com/apikey)
echo 'export GEMINI_API_KEY="your_key_here"' >> ~/.zshrc
source ~/.zshrc

# 4. Generate an image
python3 ~/.claude/skills/imagegen-gemini/scripts/generate_image.py "A sunset over mountains" -o sunset.png
```

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

#### Option 1: Global Install (available in all projects)

```bash
# Clone to global Claude skills directory
git clone https://github.com/bhaidar/imagegen-gemini.git ~/.claude/skills/imagegen-gemini

# Install Python dependencies
pip3 install -r ~/.claude/skills/imagegen-gemini/requirements.txt

# Set API key in your shell profile (~/.bashrc or ~/.zshrc)
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

#### Option 2: Project Install (available in current project only)

```bash
# Clone to project's Claude skills directory
git clone https://github.com/bhaidar/imagegen-gemini.git .claude/skills/imagegen-gemini

# Install Python dependencies
pip3 install -r .claude/skills/imagegen-gemini/requirements.txt

# Set API key in your shell profile (~/.bashrc or ~/.zshrc)
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

**Note:** After installation, restart your terminal or run `source ~/.zshrc` (or `~/.bashrc`) for the API key to take effect.

### For Claude.ai (Web/App)

1. Download this repo as a ZIP
2. Go to Settings > Capabilities > Skills
3. Click "Upload skill" and select the ZIP file
4. The skill will prompt you for the API key if needed

### API Key Setup

Get your free API key at: https://aistudio.google.com/apikey

**Important:** The free tier has rate limits. See [Troubleshooting](#troubleshooting) for quota issues.

### Standalone Usage

```bash
git clone https://github.com/bhaidar/imagegen-gemini.git
cd imagegen-gemini
pip3 install -r requirements.txt
export GEMINI_API_KEY="your_api_key_here"
```

### Verifying Installation

Test the installation:
```bash
python3 ~/.claude/skills/imagegen-gemini/scripts/generate_image.py "test image" -o test.png --json
```

If successful, you should see:
```json
{
  "success": true,
  "path": "/absolute/path/to/test.png",
  "model": "gemini-2.5-flash-image"
}
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
| `flash` | gemini-2.5-flash | Fast, general purpose (default) |
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
Then restart your terminal or run `source ~/.zshrc` (or `~/.bashrc`).

### "429 RESOURCE_EXHAUSTED" or "Quota exceeded"
You've hit the free tier rate limit. Solutions:
- **Wait:** The error message shows retry time (e.g., "Please retry in 47s")
- **Upgrade:** Consider upgrading to a paid plan at https://ai.google.dev/pricing
- **Monitor usage:** Check current usage at https://ai.dev/rate-limit
- **Use different model:** Try `-m flash` instead of `-m flash-image`

Free tier limits (as of 2026):
- Requests per day: Varies by model
- Requests per minute: Limited
- Check current limits: https://ai.google.dev/gemini-api/docs/rate-limits

### "404 NOT_FOUND" or "model is not found"
The model name may have changed. Try:
- Use `-m flash-image` (recommended for image generation)
- Use `-m pro-image` (highest quality, but may have stricter limits)

### "No image generated"
Some prompts may be blocked by safety filters. Try:
- Rephrasing your prompt
- Being more specific and descriptive
- Avoiding potentially sensitive content

### Installation Issues

**Dependencies not installed:**
```bash
pip3 install -r requirements.txt
```

**Permission errors on macOS/Linux:**
```bash
pip3 install --user -r requirements.txt
```

**Python not found:**
Make sure Python 3.9+ is installed:
```bash
python3 --version
```

## License

MIT License. See [LICENSE](LICENSE) for details.

## Links

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Get API Key](https://aistudio.google.com/apikey)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
