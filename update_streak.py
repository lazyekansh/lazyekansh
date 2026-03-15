#!/usr/bin/env python3
import urllib.request
import json
import datetime

USERNAME = 'lazyekansh'

# === TERMINAL COLOR THEME ===
COLOR_CYAN    = "#00f3ff"
COLOR_PINK    = "#ff0055"
COLOR_WHITE   = "#ffffff"
COLOR_BG_DARK = "#0d1117"
COLOR_BG_ROW  = "#111827"
COLOR_BORDER  = "#00f3ff"

def get_contributions_data():
    url = f'https://github-contributions-api.jogruber.de/v4/{USERNAME}?y={datetime.date.today().year}'
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def calculate_stats(data):
    if not data:
        return 0, 0
    total = data.get('total', {}).get(str(datetime.date.today().year), 0)
    days = data.get('contributions', [])

    contrib_dict = {day['date']: day['count'] for day in days}

    today = datetime.date.today()
    streak = 0
    current_date = today
    while True:
        count = contrib_dict.get(current_date.isoformat(), 0)
        if count > 0:
            streak += 1
            current_date -= datetime.timedelta(days=1)
        else:
            break

    return total, streak

def get_status_data(streak, days_since_last=0):
    # Sprite selection
    if streak >= 30:
        sprite = "wooper_play.gif"
    elif streak >= 7:
        sprite = "wooper_idle.gif"
    elif streak >= 1:
        sprite = "wooper_idle.gif"
    else:
        sprite = "wooper_sad.gif"

    # Status text — lazyekansh flavoured
    if streak == 0:
        if days_since_last <= 1:
            text = "signal lost. reconnecting..."
        elif days_since_last <= 3:
            text = "kernel idle. touching grass."
        elif days_since_last <= 7:
            text = "offline mode. i'll be back."
        else:
            text = "system dormant. reboot imminent."
    elif streak == 1:
        text = "link restored. back in the terminal."
    elif streak <= 6:
        text = "commit stream active. flow state engaged."
    elif streak <= 29:
        text = "shipping daily. no days off."
    else:
        text = "god mode. the streak is real."

    return sprite, text

def update_readme(sprite, status_text, total, streak):
    readme_path = 'README.md'
    try:
        with open(readme_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return

    start_marker = '<!-- TABLE-START -->'
    end_marker   = '<!-- TABLE-END -->'

    start = content.find(start_marker)
    end   = content.find(end_marker)

    if start == -1 or end == -1:
        return

    before = content[:start]
    after  = content[end + len(end_marker):]

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

    new_html = f'''<!-- Last updated: {timestamp} -->
<div align="center">
  <table style="border: 1px solid {COLOR_BORDER}; border-radius: 0px; background: {COLOR_BG_DARK}; width: 80%; box-shadow: 0 0 12px {COLOR_BORDER}50;">
    <tr style="border-bottom: 1px solid {COLOR_BORDER};">
      <td colspan="2" style="padding: 8px; background: {COLOR_BG_ROW}; color: {COLOR_CYAN}; font-family: monospace; font-size: 12px;">
        lazyekansh @ github :: ~/status
      </td>
    </tr>
    <tr>
      <td align="center" style="padding: 20px; border-right: 1px solid {COLOR_BORDER}; width: 40%; vertical-align: middle;">
        <img src="sprites/{sprite}" alt="Pet" width="180" style="image-rendering: pixelated; filter: drop-shadow(0 0 6px {COLOR_CYAN});" />
        <br><br>
        <code style="color: {COLOR_CYAN};">{status_text}</code>
      </td>
      <td align="left" style="padding: 20px; font-family: 'Courier New', monospace; color: {COLOR_WHITE};">
        <strong style="color: {COLOR_CYAN};">// system_metrics</strong><br><br>
        streak_active :: <code style="color: {COLOR_CYAN};">{streak} days</code><br>
        total_commits&nbsp;&nbsp;:: <code style="color: {COLOR_CYAN};">{total}</code><br>
        current_year&nbsp;&nbsp;&nbsp;:: <code style="color: {COLOR_CYAN};">{datetime.date.today().year}</code><br>
      </td>
    </tr>
  </table>
</div>
'''

    with open(readme_path, 'w') as f:
        f.write(before + start_marker + new_html + end_marker + after)

if __name__ == '__main__':
    data = get_contributions_data()
    if data:
        total, streak = calculate_stats(data)

        days_list = data.get('contributions', [])
        days_list.sort(key=lambda x: x['date'], reverse=True)
        days_since = 0
        for d in days_list:
            if d['count'] == 0:
                days_since += 1
            else:
                break

        sprite, text = get_status_data(streak, days_since)
        update_readme(sprite, text, total, streak)
        print(f"Updated: streak={streak}, total={total}, sprite={sprite}")
