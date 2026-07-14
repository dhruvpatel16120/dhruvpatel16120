from PIL import Image, ImageEnhance
import os

def image_to_ascii(image_path, width=92, height=53, contrast_factor=1.6, brightness_factor=1.0):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} does not exist.")
        return None
    
    # Load image
    img = Image.open(image_path)
    
    # 1. Background Suppression / Contrast Tuning
    # Let's crop slightly if needed, but since it's already square-ish, we will resize it directly
    # We want to enhance the contrast to make the facial features and hair pop out.
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast_factor)
    
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness_factor)
    
    # Convert to grayscale
    img_gray = img.convert("L")
    
    # Resize to the target grid (92x53)
    img_resized = img_gray.resize((width, height), Image.Resampling.LANCZOS)
    
    # ASCII character mapping from dark (filled) to light (empty)
    # Sushmita's characters: '%', '*', '+', '=', '-', ':', '.', ' '
    chars = ["%", "*", "+", "=", "-", ":", ".", " "]
    num_chars = len(chars)
    
    ascii_lines = []
    for y in range(height):
        line_chars = []
        for x in range(width):
            pixel = img_resized.getpixel((x, y))
            # Map pixel (0-255) to character index (0 to num_chars - 1)
            char_idx = min(int(pixel / 256 * num_chars), num_chars - 1)
            line_chars.append(chars[char_idx])
        ascii_lines.append("".join(line_chars))
        
    return ascii_lines

def generate_tspans(ascii_lines, start_x=30, start_y=79.98, line_height=7.55):
    from html import escape
    
    tspan_lines = []
    y = start_y
    for line in ascii_lines:
        # Escape HTML special characters
        escaped_line = escape(line)
        tspan_lines.append(
            f'<tspan x="{start_x}" y="{y:.2f}" xml:space="preserve">{escaped_line}</tspan>'
        )
        y += line_height
        
    return tspan_lines

if __name__ == "__main__":
    # Path to the user's profile image
    base_dir = r"c:\Users\digit\OneDrive\Desktop\github profile"
    img_path = os.path.join(base_dir, "profile.png")
    
    # Output paths inside user's directory
    output_dir = os.path.join(base_dir, "dhruvpatel16120")
    txt_path = os.path.join(output_dir, "portrait.txt")
    tspan_path = os.path.join(output_dir, "portrait_tspan.txt")
    
    print(f"Processing image: {img_path}...")
    
    # Run conversion
    # We can tune contrast_factor to make details look sharp and screen out background
    ascii_lines = image_to_ascii(img_path, contrast_factor=1.75, brightness_factor=0.95)
    
    if ascii_lines:
        # Write portrait.txt
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(ascii_lines))
        print(f"Generated raw ASCII art in: {txt_path}")
        
        # Write portrait_tspan.txt
        tspan_lines = generate_tspans(ascii_lines)
        with open(tspan_path, "w", encoding="utf-8") as f:
            f.write("\n".join(tspan_lines))
        print(f"Generated SVG tspan file in: {tspan_path}")
        
        # Print a small preview to console
        print("\nASCII Preview (first 10 lines):")
        for line in ascii_lines[:15]:
            print(line)
