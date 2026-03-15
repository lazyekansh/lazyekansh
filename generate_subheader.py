# generate_subheader.py
def create_typing_svg():
    text = "full stack dev; osint tooling; ai systems; chess 1613 rapid"
    filename = "subheader_typing.svg"

    color_cyan = "#00f3ff"

    safe_text = text.replace("&", "&amp;")
    chars = len(text)
    svg_width = 1000

    svg_content = f'''<svg width="{svg_width}" height="60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@500&amp;display=swap');

      .container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        width: 100%;
      }}

      .typing-text {{
        font-family: 'Fira Code', monospace;
        font-size: 22px;
        color: {color_cyan};

        width: 0;
        white-space: nowrap;
        overflow: hidden;
        border-right: 4px solid {color_cyan};

        animation:
          typing 8s steps({chars}, end) infinite,
          blink 0.8s step-end infinite;

        text-shadow: 0 0 5px {color_cyan}80;
      }}

      @keyframes typing {{
        0% {{ width: 0ch; }}
        40% {{ width: {chars}ch; }}
        90% {{ width: {chars}ch; }}
        100% {{ width: 0ch; }}
      }}

      @keyframes blink {{
        0%, 100% {{ border-color: transparent; }}
        50% {{ border-color: {color_cyan}; }}
      }}
    </style>
  </defs>

  <foreignObject x="0" y="0" width="{svg_width}" height="60">
    <div xmlns="http://www.w3.org/1999/xhtml" class="container">
        <span class="typing-text">{safe_text}</span>
    </div>
  </foreignObject>
</svg>'''

    with open(filename, "w") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    create_typing_svg()
