import os

def load_tspan(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"ASCII tspan file not found at {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def build_terminal_line(key, value, y_coord, total_dots_target=19):
    # Format subkeys like 'Net.Languages' with custom formatting
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
    bg_glow_stop0 = "#0D0B21" if is_dark else "#FDF2F8"
    bg_glow_stop1 = "#05040B" if is_dark else "#F3E8FF"
    bg_glow_stop2 = "#020205" if is_dark else "#E0F2FE"
    
    ascii_grad_stop0 = "#FF007F" if is_dark else "#8B5CF6"
    ascii_grad_values = "#FF007F;#00F3FF;#FFE600;#FF007F" if is_dark else "#8B5CF6;#EC4899;#0EA5E9;#8B5CF6"
    
    ascii_grad_stop1 = "#00F3FF" if is_dark else "#EC4899"
    ascii_grad_values1 = "#00F3FF;#FFE600;#FF007F;#00F3FF" if is_dark else "#EC4899;#0EA5E9;#8B5CF6;#EC4899"
    
    border_grad_stop0 = "#FF007F" if is_dark else "#8B5CF6"
    border_grad_stop1 = "#00F3FF" if is_dark else "#EC4899"
    border_grad_stop2 = "#FFE600" if is_dark else "#0EA5E9"
    
    scan_grad_stop0 = "#00F3FF" if is_dark else "#EC4899"
    scan_grad_opacity_stop0 = "0.08" if is_dark else "0.06"
    scan_grad_stop1 = "#FFE600" if is_dark else "#FBCFE8"
    scan_grad_opacity_stop1 = "0.75" if is_dark else "0.45"
    scan_grad_stop2 = "#FF007F" if is_dark else "#8B5CF6"
    
    scanlines_fill = "#00F3FF" if is_dark else "#475569"
    scanlines_opacity = "0.06" if is_dark else "0.03"
    
    # Styles
    ascii_fill = "url(#asciiGrad)"
    key_fill = "#00F3FF" if is_dark else "#7C3AED"
    value_fill = "#E2E8F0" if is_dark else "#1E293B"
    cc_fill = "#5F5B8B" if is_dark else "#94A3B8"
    head_fill = "#FF007F" if is_dark else "#DB2777"
    accent_fill = "#FFE600" if is_dark else "#0EA5E9"
    cursor_fill = "#00F3FF" if is_dark else "#D946EF"
    
    term_label_fill = "#8F8CAE" if is_dark else "#64748B"
    scan_label_fill = "#FF007F" if is_dark else "#DC2626"
    panel_title_fill = "#00F3FF" if is_dark else "#7C3AED"
    panel_title_opacity = "0.85" if is_dark else "0.75"
    
    titlebar_bg = "#070614" if is_dark else "#FFFFFF"
    titlebar_opacity = "0.9" if is_dark else "0.85"
    
    panel_bg = "#03020A" if is_dark else "#FFFFFF"
    panel_bg_opacity = "0.55" if is_dark else "0.45"
    panel_border_opacity = "0.5" if is_dark else "0.3"
    
    scan_blend_mode = "screen" if is_dark else "multiply"
    scan_rect_opacity = "0.8" if is_dark else "0.6"
    
    global_border_opacity = "0.95" if is_dark else "0.8"
    
    text_color_main = "#E2E8F0" if is_dark else "#1E293B"
    
    # Generate system info lines
    lines = [
        # Line 0: Header
        f'<tspan x="520" y="42" class="head">dhruvpatel16120@cybernet</tspan><tspan class="cc"> --————————————————————————————————————-</tspan>',
        # Line 1: Subject
        build_terminal_line("Subject", "Dhruv Patel", 66),
        # Line 2: Title
        build_terminal_line("Title", "Aspiring Data Scientist | AI Engineer", 88),
        # Line 3: Node
        build_terminal_line("Node", "Rajkot, Gujarat, India (GMT +5:30)", 110),
        # Line 4: Class
        build_terminal_line("Class", "B.E. AI &amp; Data Science (GECR)", 132),
        # Line 5: Status
        build_terminal_line("Status", "GSSoC 2026 Open Source Contribution", 154),
        # Line 6: Net.Level
        build_terminal_line("Net.Level", "Intermediate", 176),
        # Line 7: Availability
        build_terminal_line("Avail.", "Open to Work | Internship", 198),
        # Line 8: Empty (space after header section)
        f'<tspan x="520" y="220" class="cc">. </tspan>',
        # Line 9: Net.Languages
        build_terminal_line("Net.Languages", "Python (Primary), SQL, JavaScript", 242),
        # Line 10: Net.AI
        build_terminal_line("Net.AI", "LangChain, RAG, Gemini API, Prompt Eng", 264),
        # Line 11: Net.DataScience
        build_terminal_line("Net.DataScience", "NumPy, Pandas, Scikit-learn, Seaborn", 286),
        # Line 12: Net.Stack
        build_terminal_line("Net.Stack", "FastAPI, Next.js, Streamlit", 308),
        # Line 13: Net.Databases
        build_terminal_line("Net.Databases", "PostgreSQL, Firebase, MySQL", 330),
        # Line 14: Empty (space above connect.channels)
        f'<tspan x="520" y="352" class="cc">. </tspan>',
        # Line 15: Contact Header
        f'<tspan x="520" y="374" class="accent">[ CONNECT.CHANNELS ]</tspan><tspan class="cc"> -————————————————————————————————————--</tspan>',
        # Line 16: Comms.Mail
        build_terminal_line("Comms.Mail", "dhruvpatel16120@gmail.com", 396),
        # Line 17: Comms.Web
        build_terminal_line("Comms.Web", "dhruvpatelofficial.vercel.app", 418),
        # Line 18: Comms.LinkedIn
        build_terminal_line("Comms.LinkedIn", "linkedin.com/in/dhruvpatel16120", 440),
        # Line 19: Comms.Terminal
        build_terminal_line("Comms.Terminal", "github.com/dhruvpatel16120", 462),
        # Line 20: Empty
        f'<tspan x="520" y="484" class="cc">. </tspan>',
        # Line 21: Linus Torvalds developer quote
        f'<tspan x="520" y="506" class="cc">" </tspan><tspan class="accent">Talk is cheap. Show me the code.</tspan><tspan class="cc"> " — Linus Torvalds</tspan>'
    ]
    
    # Build lines with clip paths
    text_elements = []
    y_coords = [42, 66, 88, 110, 132, 154, 176, 198, 220, 242, 264, 286, 308, 330, 352, 374, 396, 418, 440, 462, 484, 506]
    
    for idx, (coord, content) in enumerate(zip(y_coords, lines)):
        text_elements.append(
            f'<g clip-path="url(#lc{idx})"><text x="520" y="0" fill="{text_color_main}">{content}</text></g>'
        )
        
    text_section = "".join(text_elements)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="628" viewBox="0 0 1180 628">
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
  <radialGradient id="bgGlow" cx="50%" cy="50%" r="75%">
    <stop offset="0%" stop-color="{bg_glow_stop0}"/>
    <stop offset="60%" stop-color="{bg_glow_stop1}"/>
    <stop offset="100%" stop-color="{bg_glow_stop2}"/>
  </radialGradient>
  <linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{scan_grad_stop0}" stop-opacity="0"/>
    <stop offset="45%" stop-color="{scan_grad_stop0}" stop-opacity="{scan_grad_opacity_stop0}"/>
    <stop offset="50%" stop-color="{scan_grad_stop1}" stop-opacity="{scan_grad_opacity_stop1}"/>
    <stop offset="55%" stop-color="{scan_grad_stop2}" stop-opacity="{scan_grad_opacity_stop0}"/>
    <stop offset="100%" stop-color="{scan_grad_stop2}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="{scanlines_fill}" opacity="{scanlines_opacity}"/>
  </pattern>
  <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="5" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <filter id="neonNeon" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur1"/>
    <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur2"/>
    <feMerge>
      <feMergeNode in="blur2"/>
      <feMergeNode in="blur1"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <mask id="revealMask" maskUnits="userSpaceOnUse" x="0" y="0" width="1180" height="620">
    <rect x="0" y="0" width="1180" height="0" fill="#fff">
      <animate attributeName="height" from="0" to="580" dur="2.6s" begin="0.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
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
    .head   {{ font-family: 'Courier New', Consolas, monospace; font-size: 17px; fill: {head_fill}; font-weight: bold; text-shadow: 0 0 5px {head_fill}; }}
    .accent {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: {accent_fill}; font-weight: bold; text-shadow: 0 0 5px {accent_fill}; }}
    text, tspan {{ white-space: pre; }}
    
    .term-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 12px; fill: {term_label_fill}; letter-spacing: 0.5px; }}
    .scan-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 10px; fill: {scan_label_fill}; letter-spacing: 1px; animation: blinker 1s steps(2, start) infinite; }}
    .panel-title {{ font-family: 'Courier New', Consolas, monospace; font-size: 11px; fill: {panel_title_fill}; letter-spacing: 2px; opacity: {panel_title_opacity}; }}
    .cursor-blink {{ fill: {cursor_fill}; }}
    
    .neon-pulsing-border {{
      stroke: url(#borderGrad);
      stroke-width: 2px;
      animation: neonPulse 3.5s infinite alternate;
    }}
    
    .flicker-deck {{
      animation: deckFlicker 6s infinite alternate;
    }}
    
    @keyframes neonPulse {{
      0% {{ filter: drop-shadow(0 0 2px rgba(255, 0, 127, 0.45)) drop-shadow(0 0 6px rgba(0, 243, 255, 0.25)); opacity: 0.85; }}
      100% {{ filter: drop-shadow(0 0 6px rgba(255, 0, 127, 0.85)) drop-shadow(0 0 16px rgba(0, 243, 255, 0.55)); opacity: 0.98; }}
    }}
    
    @keyframes deckFlicker {{
      0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {{ opacity: 0.99; filter: drop-shadow(0 0 3px rgba(0, 243, 255, 0.5)); }}
      20%, 24%, 55% {{ opacity: 0.75; filter: none; }}
    }}

    @keyframes blinker {{
      to {{ opacity: 0; }}
    }}
  </style>
</defs>

<rect width="1180" height="628" rx="18" fill="url(#bgGlow)"/>
<rect width="1180" height="628" rx="18" fill="url(#scanlines)"/>

<g id="titlebar">
  <rect x="3" y="3" width="1174" height="34" rx="16" fill="{titlebar_bg}" fill-opacity="{titlebar_opacity}" class="neon-pulsing-border"/>
  <circle cx="24" cy="20" r="5" fill="#EF4444"><animate attributeName="opacity" values="1;0.55;1" dur="4s" repeatCount="indefinite"/></circle>
  <circle cx="42" cy="20" r="5" fill="#FBBF24"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.3s" repeatCount="indefinite"/></circle>
  <circle cx="60" cy="20" r="5" fill="#34D399"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.6s" repeatCount="indefinite"/></circle>
  <text x="590" y="25" text-anchor="middle" class="term-label flicker-deck">dhruvpatel16120@cyberdeck ~ % ./info.sh --interactive</text>
  <circle cx="1122" cy="20" r="4" fill="{scan_label_fill}">
    <animate attributeName="opacity" values="1;0.15;1" dur="1.1s" repeatCount="indefinite"/>
  </circle>
  <text x="1132" y="24" class="scan-label">ACTIVE.NODE</text>
</g>

<g transform="translate(0,38)">
  <rect x="14" y="26" width="488" height="490" rx="14" fill="{panel_bg}" fill-opacity="{panel_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1.5" class="neon-pulsing-border" opacity="{panel_border_opacity}"/>
  <rect x="508" y="10" width="655" height="524" rx="14" fill="{panel_bg}" fill-opacity="{panel_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1.5" class="neon-pulsing-border" opacity="{panel_border_opacity}"/>
  <text x="30" y="24" class="panel-title flicker-deck">[ BIO.PROFILE ]</text>
  <text x="524" y="24" class="panel-title flicker-deck">[ SYSTEM.DIAGNOSTICS ]</text>

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

<rect x="3" y="3" width="1174" height="622" rx="16" fill="none" class="neon-pulsing-border" opacity="{global_border_opacity}"/>

<rect x="0" y="-70" width="1180" height="70" fill="url(#scanGrad)" opacity="{scan_rect_opacity}" style="mix-blend-mode:{scan_blend_mode}">
  <animateTransform attributeName="transform" type="translate" from="0 -70" to="0 698" dur="4.5s" repeatCount="indefinite"/>
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
