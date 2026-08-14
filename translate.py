import os
import glob
import re
from deep_translator import GoogleTranslator

os.makedirs('cy', exist_ok=True)
translator = GoogleTranslator(source='en', target='cy')

def chunk_and_translate(text):
    paragraphs = text.split('\n\n')
    translated = []
    for p in paragraphs:
        if p.strip():
            try:
                res = translator.translate(p)
                if res is None:
                    translated.append(p)
                else:
                    translated.append(res)
            except Exception as e:
                print(f"    [!] Error: {e}")
                translated.append(p)
        else:
            translated.append(p)
    return '\n\n'.join(translated)

files_to_process = []
for ext in ('**/*.md', '**/*.html'):
    files_to_process.extend(glob.glob(ext, recursive=True))

for filepath in files_to_process:
    filepath = filepath.replace('\\', '/')
    
    if filepath.startswith('cy/') or filepath.startswith('_site/') or 'README.md' in filepath:
        continue
        
    print(f"Translating: {filepath}...")
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'^(---.*?---)', content, flags=re.MULTILINE | re.DOTALL)
    
    translated_content = ""
    for part in parts:
        if part.startswith('---'):
            if 'permalink:' in part:
                part = re.sub(r'(permalink:\s*)/(.+)', r'\1/cy/\2', part)
            translated_content += part
        elif part.strip():
            translated_content += chunk_and_translate(part)
        else:
            translated_content += part

    out_filepath = f'cy/{filepath}'
    os.makedirs(os.path.dirname(out_filepath), exist_ok=True)

    with open(out_filepath, 'w', encoding='utf-8') as f:
        f.write(translated_content)

print("Translation complete!")