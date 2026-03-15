# generate_header.py
def create_glitch_svg():
    text = "lazyekansh"
    filename = "header_glitch.svg"

    color_main = "#ffffff"
    color_cyan = "#00f3ff"
    color_pink = "#ff0055"

    svg_content = f'''<svg width="800" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&amp;display=swap');

      .glitch-text {{
          font-family: 'Fira Code', 'Consolas', 'Menlo', monospace;
          font-weight: 700;
          font-size: 70px;
          text-transform: lowercase;
          letter-spacing: -2px;
      }}

      .layer-main {{ fill: {color_main}; }}

      .layer-cyan {{
          fill: {color_cyan};
          mix-blend-mode: screen;
          animation: glitch-anim-1 2.5s infinite linear alternate-reverse;
          opacity: 0.8;
      }}

      .layer-pink {{
          fill: {color_pink};
          mix-blend-mode: screen;
          animation: glitch-anim-2 3s infinite linear alternate-reverse;
          opacity: 0.8;
      }}

      @keyframes glitch-anim-1 {{
          0% {{ transform: translate(0); }}
          20% {{ transform: translate(-4px, 2px); }}
          40% {{ transform: translate(-4px, -2px); }}
          60% {{ transform: translate(4px, 2px); }}
          80% {{ transform: translate(4px, -2px); }}
          100% {{ transform: translate(0); }}
      }}

      @keyframes glitch-anim-2 {{
          0% {{ transform: translate(0); }}
          25% {{ transform: translate(4px, -2px); }}
          50% {{ transform: translate(4px, 2px); }}
          75% {{ transform: translate(-4px, -4px); }}
          100% {{ transform: translate(0); }}
      }}
    </style>
  </defs>

  <g transform="translate(400, 80)" text-anchor="middle">
    <text class="glitch-text layer-cyan">{text}</text>
    <text class="glitch-text layer-pink">{text}</text>
    <text class="glitch-text layer-main">{text}</text>
  </g>
</svg>'''

    with open(filename, "w") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    create_glitch_svg()
