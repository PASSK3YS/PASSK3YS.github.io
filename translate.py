import os
import glob
import re
from deep_translator import MyMemoryTranslator

os.makedirs('cy', exist_ok=True)
translator = MyMemoryTranslator(source='en-GB', target='cy-GB')

for filepath in glob.glob('*.md'):
    if filepath == 'README.md' or filepath.startswith('cy/'):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'^(---.*?---)', content, flags=re.MULTILINE | re.DOTALL)
    
    translated_content = ""
    for part in parts:
        if part.startswith('---'):
            translated_content += part
        elif part.strip():
            try:
                translated_content += translator.translate(part)
            except:
                translated_content += part
        else:
            translated_content += part

    with open(f'cy/{filepath}', 'w', encoding='utf-8') as f:
        f.write(translated_content)