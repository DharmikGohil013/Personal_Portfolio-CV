import urllib.request

url = 'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css'
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
    print("Fetched CSS successfully. Length:", len(html))
    
    # Find @font-face
    font_face_start = html.find('@font-face')
    if font_face_start != -1:
        font_face_end = html.find('}', font_face_start)
        print("Font Face Rule:")
        print(html[font_face_start:font_face_end+1])
    else:
        print("No @font-face found in the first pass.")
        print(html[:500])
except Exception as e:
    print("Error:", e)
