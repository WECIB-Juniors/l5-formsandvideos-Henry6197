import re

# Read the file
with open('assignment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all color options
pattern = r'<option value="(#[0-9A-Fa-f]{6})" style="background-color: (#[0-9A-Fa-f]{6}); color: (white|black);">(.*?)</option>'
matches = re.findall(pattern, content)

# Collect colors (skip empty select option)
colors = []
for match in matches:
    if match[0] != '':
        hex_color = match[0]
        name = match[3]
        colors.append((hex_color, name))

# Convert hex to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Convert RGB to HSV for rainbow sorting
def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    s = 0 if mx == 0 else df/mx
    v = mx
    return h, s, v

# Sort colors by hue, then saturation, then value for a smooth rainbow gradient
sorted_colors = sorted(colors, key=lambda x: rgb_to_hsv(*hex_to_rgb(x[0])))

# Replace the last color with custom 1067 color
sorted_colors[-1] = ('#106710', '1067!!!!!!!!!!!!')

# Generate new options HTML
options_html = '                <option value="">Select</option>\n'
for hex_color, name in sorted_colors:
    r, g, b = hex_to_rgb(hex_color)
    # Calculate luminance for text color
    text_color = 'white' if (r*0.299 + g*0.587 + b*0.114) < 128 else 'black'
    options_html += f'                <option value="{hex_color}" style="background-color: {hex_color}; color: {text_color};">{name}</option>\n'

# Find the select tag and replace its contents
select_pattern = r'(<select id="favorite-color" name="favorite-color">)(.*?)(</select>)'
new_content = re.sub(select_pattern, r'\1\n' + options_html + '            \3', content, flags=re.DOTALL)

# Write back
with open('assignment.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Successfully reorganized {len(sorted_colors)} colors into a rainbow gradient!')
print(f'Last color is now: 1067!!!!!!!!!!!!! ({sorted_colors[-1][0]})')
