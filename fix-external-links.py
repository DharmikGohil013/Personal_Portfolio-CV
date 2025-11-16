import re

# Read the file
with open('Achivemtn.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Replace all external links that don't have rel="noopener noreferrer"
# Pattern: target="_blank" not followed by rel="noopener noreferrer"
pattern = r'target="_blank"(?!\s*rel="noopener noreferrer")'
replacement = r'target="_blank" rel="noopener noreferrer"'

updated_content = re.sub(pattern, replacement, content)

# Write back
with open('Achivemtn.html', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("✅ All external links updated with rel='noopener noreferrer'")
print(f"Updated {len(re.findall(pattern, content))} links")
