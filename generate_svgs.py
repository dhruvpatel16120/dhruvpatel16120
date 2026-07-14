import os

def load_tspan(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"ASCII tspan file not found at {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def build_terminal_line(key, value, y_coord, total_dots_target=18):
    # If key contains a subkey like 'Core.Lang', let's format it with split keys
    # Example: <tspan class="key">Core</tspan><tspan class="cc">.</tspan><tspan class="key">Lang</tspan>
    parts = key.split('.')
    if len(parts) > 1:
        key_html = f'<tspan class="key">{parts[0]}</tspan><tspan class="cc">.</tspan><tspan class="key">{parts[1]}</tspan>'
        key_len = len(parts[0]) + 1 + len(parts[1])
    else:
        key_html = f'<tspan class="key">{key}</tspan>'
        key_len = len(key)
        
    dots_count = max(total_dots_target - key_len, 2)
    dots = "." * dots_count
    
    return f'<tspan x="520" y="{y_coord}" class="cc">. </tspan>{key_html}<tspan class="cc">: {dots} </tspan><tspan class="value">{value}</tspan>'

def generate_svg(ascii_tspans, theme="dark"):
    is_dark = theme == "dark"
    
    # Theme configuration
    bg_glow_stop0 = "#0B1120" if is_dark else "#F8FAFC"
    bg_glow_stop1 = "#050816" if is_dark else "#E2E8F0"
    
    ascii_grad_stop0 = "#22D3EE" if is_dark else "#4F46E5"
    ascii_grad_values = "#22D3EE;#7C3AED;#38BDF8;#22D3EE" if is_dark else "#4F46E5;#7C3AED;#0EA5E9;#4F46E5"
    
    ascii_grad_stop1 = "#7C3AED" if is_dark else "#7C3AED"
    ascii_grad_values1 = "#7C3AED;#38BDF8;#22D3EE;#7C3AED" if is_dark else "#7C3AED;#0EA5E9;#4F46E5;#7C3AED"
    
    border_grad_stop0 = "#7C3AED"
    border_grad_stop1 = "#22D3EE" if is_dark else "#0EA5E9"
    border_grad_stop2 = "#10B981" if is_dark else "#059669"
    
    scan_grad_stop0 = "#22D3EE" if is_dark else "#0EA5E9"
    scan_grad_opacity_stop0 = "0.05" if is_dark else "0.06"
    scan_grad_stop1 = "#A5F3FC" if is_dark else "#38BDF8"
    scan_grad_opacity_stop1 = "0.65" if is_dark else "0.55"
    scan_grad_stop2 = "#7C3AED"
    
    scanlines_fill = "#7DD3FC" if is_dark else "#334155"
    scanlines_opacity = "0.05" if is_dark else "0.035"
    
    # Styles
    ascii_fill = "url(#asciiGrad)"
    key_fill = "#22D3EE" if is_dark else "#0284C7"
    value_fill = "#E5E7EB" if is_dark else "#1E293B"
    cc_fill = "#475569" if is_dark else "#94A3B8"
    head_fill = "#7C3AED"
    accent_fill = "#10B981" if is_dark else "#059669"
    cursor_fill = "#22D3EE" if is_dark else "#0EA5E9"
    
    term_label_fill = "#64748B"
    scan_label_fill = "#F87171" if is_dark else "#DC2626"
    panel_title_fill = "#38BDF8" if is_dark else "#0284C7"
    panel_title_opacity = "0.7" if is_dark else "0.75"
    
    titlebar_bg = "#0B1120" if is_dark else "#FFFFFF"
    titlebar_opacity = "0.85" if is_dark else "0.9"
    
    panel_bg = "#0B1120" if is_dark else "#FFFFFF"
    panel_bg_opacity = "0.35" if is_dark else "0.55"
    panel_border_opacity = "0.35" if is_dark else "0.4"
    
    scan_blend_mode = "screen" if is_dark else "multiply"
    scan_rect_opacity = "0.7" if is_dark else "0.8"
    
    global_border_opacity = "0.8" if is_dark else "0.75"
    global_border_anim = "0.5;0.95;0.5" if is_dark else "0.45;0.9;0.45"
    
    text_color_main = "#dbeafe" if is_dark else "#1E293B"
    
    # Generate system info lines
    lines = [
        # Line 0: Header
        f'<tspan x="520" y="42" class="head">dhruv@devos</tspan><tspan class="cc"> -——————————————————————————————————————————-—-</tspan>',
        # Line 1: Subject
        build_terminal_line("Subject", "Dhruv Patel", 66),
        # Line 2: Role
        build_terminal_line("Role", "CSE Student &amp; AI/ML Explorer", 88),
        # Line 3: Origin
        build_terminal_line("Origin", "India", 110),
        # Line 4: Education
        build_terminal_line("Education", "B.Tech CSE (AI &amp; DS)", 132),
        # Line 5: Status
        build_terminal_line("Status", "Learning • Building • Innovating", 154),
        # Line 6: ToolChain
        build_terminal_line("ToolChain", "VS Code, Git, GitHub, Jupyter", 176),
        # Line 7: Empty
        f'<tspan x="520" y="198" class="cc">. </tspan>',
        # Line 8: Core.Lang
        build_terminal_line("Core.Lang", "Python, SQL, JavaScript, HTML, CSS", 220),
        # Line 9: Core.Frontend
        build_terminal_line("Core.Frontend", "React, Next.js, Tailwind CSS", 242),
        # Line 10: Core.Backend
        build_terminal_line("Core.Backend", "FastAPI, Streamlit, Django, Node.js", 264),
        # Line 11: Core.Database
        build_terminal_line("Core.Database", "PostgreSQL, Firebase, MySQL", 286),
        # Line 12: Core.Infra
        build_terminal_line("Core.Infra", "Git, GitHub, Hugging Face, Kaggle", 308),
        # Line 13: Empty
        f'<tspan x="520" y="330" class="cc">. </tspan>',
        # Line 14: Contact Header
        f'<tspan x="520" y="352" class="accent">- Contact</tspan><tspan class="cc"> -————————————————————————————————————————————-—-</tspan>',
        # Line 15: Grid.Mail
        build_terminal_line("Grid.Mail", "dhruvpatel16120@gmail.com", 374),
        # Line 16: Grid.Portfolio
        build_terminal_line("Grid.Portfolio", "dhruvpatelofficial.vercel.app", 396),
        # Line 17: Grid.LinkedIn
        build_terminal_line("Grid.LinkedIn", "dhruvpatel16120", 418),
        # Line 18: Grid.Github
        build_terminal_line("Grid.Github", "dhruvpatel16120", 440),
        # Line 19: Empty
        f'<tspan x="520" y="462" class="cc">. </tspan>',
        # Line 20: Live Stats Header
        f'<tspan x="520" y="484" class="accent">- Live Stats</tspan><tspan class="cc"> -————————————————————————————————————————————-—-</tspan>',
        # Line 21: Live Stats Link
        f'<tspan x="520" y="506" class="cc">. </tspan><tspan class="value">See live GitHub stats badges below in README ↓</tspan>'
    ]
    
    # Build lines with clip paths
    text_elements = []
    y_coords = [42, 66, 88, 110, 132, 154, 176, 198, 220, 242, 264, 286, 308, 330, 352, 374, 396, 418, 440, 462, 484, 506]
    
    for idx, (coord, content) in enumerate(zip(y_coords, lines)):
        text_elements.append(
            f'<g clip-path="url(#lc{idx})"><text x="520" y="0" fill="{text_color_main}">{content}</text></g>'
        )
        
    text_section = "".join(text_elements)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610">
<defs>
  <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{ascii_grad_stop0}">
      <animate attributeName="stop-color" values="{ascii_grad_values}" dur="9s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="{ascii_grad_stop1}">
      <animate attributeName="stop-color" values="{ascii_grad_values1}" dur="9s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>
  <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{border_grad_stop0}"/>
    <stop offset="50%" stop-color="{border_grad_stop1}"/>
    <stop offset="100%" stop-color="{border_grad_stop2}"/>
  </linearGradient>
  <radialGradient id="bgGlow" cx="30%" cy="20%" r="80%">
    <stop offset="0%" stop-color="{bg_glow_stop0}"/>
    <stop offset="100%" stop-color="{bg_glow_stop1}"/>
  </radialGradient>
  <linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{scan_grad_stop0}" stop-opacity="0"/>
    <stop offset="45%" stop-color="{scan_grad_stop0}" stop-opacity="{scan_grad_opacity_stop0}"/>
    <stop offset="50%" stop-color="{scan_grad_stop1}" stop-opacity="{scan_grad_opacity_stop1}"/>
    <stop offset="55%" stop-color="{scan_grad_stop0}" stop-opacity="{scan_grad_opacity_stop0}"/>
    <stop offset="100%" stop-color="{scan_grad_stop2}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="{scanlines_fill}" opacity="{scanlines_opacity}"/>
  </pattern>
  <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <mask id="revealMask" maskUnits="userSpaceOnUse" x="0" y="0" width="1180" height="620">
    <rect x="0" y="0" width="1180" height="0" fill="#fff">
      <animate attributeName="height" from="0" to="560" dur="2.6s" begin="0.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
    </rect>
  </mask>
  <clipPath id="lc0"><rect x="500" y="26.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="0.75s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc1"><rect x="500" y="50.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="0.86s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc2"><rect x="500" y="72.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="0.98s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc3"><rect x="500" y="94.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.09s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc4"><rect x="500" y="116.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.21s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc5"><rect x="500" y="138.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.32s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc6"><rect x="500" y="160.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.44s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc7"><rect x="500" y="182.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.55s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc8"><rect x="500" y="204.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.67s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc9"><rect x="500" y="226.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.78s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc10"><rect x="500" y="248.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="1.90s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc11"><rect x="500" y="270.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.02s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc12"><rect x="500" y="292.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.13s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc13"><rect x="500" y="314.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.25s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc14"><rect x="500" y="336.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.36s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc15"><rect x="500" y="358.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.48s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc16"><rect x="500" y="380.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.59s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc17"><rect x="500" y="402.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.71s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc18"><rect x="500" y="424.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.82s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc19"><rect x="500" y="446.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="2.94s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc20"><rect x="500" y="468.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="3.05s" fill="freeze"/></rect></clipPath>
  <clipPath id="lc21"><rect x="500" y="490.00" width="0" height="24"><animate attributeName="width" from="0" to="690" dur="0.38s" begin="3.17s" fill="freeze"/></rect></clipPath>
  <style>
    .ascii  {{ font-family: 'Courier New', Consolas, monospace; font-size: 7.4px; fill: {ascii_fill}; letter-spacing: -0.2px; }}
    .key    {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {key_fill}; font-weight: bold; }}
    .value  {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {value_fill}; }}
    .cc     {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {cc_fill}; }}
    .head   {{ font-family: 'Courier New', Consolas, monospace; font-size: 17px; fill: {head_fill}; font-weight: bold; }}
    .accent {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {accent_fill}; font-weight: bold; }}
    text, tspan {{ white-space: pre; }}
    
    .term-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 12px; fill: {term_label_fill}; letter-spacing: 0.5px; }}
    .scan-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 10px; fill: {scan_label_fill}; letter-spacing: 1px; }}
    .panel-title {{ font-family: 'Courier New', Consolas, monospace; font-size: 11px; fill: {panel_title_fill}; letter-spacing: 2px; opacity: {panel_title_opacity}; }}
    .cursor-blink {{ fill: {cursor_fill}; }}
  </style>
</defs>

<rect width="1180" height="610" rx="18" fill="url(#bgGlow)"/>
<rect width="1180" height="610" rx="18" fill="url(#scanlines)"/>

<g id="titlebar">
  <rect x="3" y="3" width="1174" height="34" rx="16" fill="{titlebar_bg}" fill-opacity="{titlebar_opacity}"/>
  <circle cx="24" cy="20" r="5" fill="#EF4444"><animate attributeName="opacity" values="1;0.55;1" dur="4s" repeatCount="indefinite"/></circle>
  <circle cx="42" cy="20" r="5" fill="#F59E0B"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.3s" repeatCount="indefinite"/></circle>
  <circle cx="60" cy="20" r="5" fill="#10B981"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.6s" repeatCount="indefinite"/></circle>
  <text x="590" y="25" text-anchor="middle" class="term-label">dhruvpatel16120@devos ~ % ./profile.sh --live</text>
  <circle cx="1122" cy="20" r="4" fill="#EF4444">
    <animate attributeName="opacity" values="1;0.15;1" dur="1.1s" repeatCount="indefinite"/>
  </circle>
  <text x="1132" y="24" class="scan-label">SCANNING</text>
</g>

<g transform="translate(0,38)">
  <rect x="14" y="26" width="488" height="468" rx="14" fill="{panel_bg}" fill-opacity="{panel_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1" opacity="{panel_border_opacity}"/>
  <rect x="508" y="10" width="655" height="500" rx="14" fill="{panel_bg}" fill-opacity="{panel_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1" opacity="{panel_border_opacity}"/>
  <text x="30" y="24" class="panel-title">VISUAL.MAP</text>
  <text x="524" y="24" class="panel-title">SYSTEM.INFO</text>

  <g mask="url(#revealMask)">
    <text x="30" y="0" class="ascii">
{ascii_tspans}
    </text>
  </g>

{text_section}

  <rect x="522" y="491.0" width="9" height="16" class="cursor-blink" opacity="0">
    <animate attributeName="opacity" values="0;0;1;0;1;0;1;0" keyTimes="0;0.01;0.02;0.3;0.5;0.7;0.85;1" dur="1.4s" begin="3.66s" repeatCount="indefinite"/>
  </rect>
</g>

<rect x="0" y="-70" width="1180" height="70" fill="url(#scanGrad)" opacity="{scan_rect_opacity}" style="mix-blend-mode:{scan_blend_mode}">
  <animateTransform attributeName="transform" type="translate" from="0 -70" to="0 680" dur="4.2s" repeatCount="indefinite"/>
</rect>

<rect x="3" y="3" width="1174" height="604" rx="16" fill="none" stroke="url(#borderGrad)" stroke-width="2" opacity="{global_border_opacity}">
  <animate attributeName="opacity" values="{global_border_anim}" dur="3.2s" repeatCount="indefinite"/>
</rect>
</svg>
"""
    return svg_content

if __name__ == "__main__":
    work_dir = r"c:\Users\digit\OneDrive\Desktop\github profile\dhruvpatel16120"
    tspan_file = os.path.join(work_dir, "portrait_tspan.txt")
    
    print(f"Loading tspans from {tspan_file}...")
    ascii_tspans = load_tspan(tspan_file)
    
    # Generate Dark SVG
    print("Generating dark.svg...")
    dark_svg = generate_svg(ascii_tspans, theme="dark")
    dark_path = os.path.join(work_dir, "dark.svg")
    with open(dark_path, "w", encoding="utf-8") as f:
        f.write(dark_svg)
    print(f"dark.svg generated successfully at {dark_path}!")
        
    # Generate Light SVG
    print("Generating light.svg...")
    light_svg = generate_svg(ascii_tspans, theme="light")
    light_path = os.path.join(work_dir, "light.svg")
    with open(light_path, "w", encoding="utf-8") as f:
        f.write(light_svg)
    print(f"light.svg generated successfully at {light_path}!")
