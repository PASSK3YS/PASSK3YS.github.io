import os
import glob
import re
from deep_translator import GoogleTranslator

os.makedirs('cy', exist_ok=True)
translator = GoogleTranslator(source='en', target='cy')

def chunk_and_translate(text):
    paragraphs = text.split('\n\n')
    translated = []
    
    protect_pattern = re.compile(r'(\{%.*?%\}|\{\{.*?\}\}|<[^>]+>|```.*?```|`.*?`)', re.DOTALL)

    for p in paragraphs:
        if not p.strip():
            translated.append(p)
            continue
            
        blocks = []
        
        # Replace the protected code with a nonsense placeholder Google won't translate
        def save_block(match):
            blocks.append(match.group(0))
            return f" ZXC{len(blocks)-1}Q "
            
        safe_p = protect_pattern.sub(save_block, p)
        
        try:
            res = translator.translate(safe_p)
            if res is None:
                translated.append(p)
            else:
                # Swap the placeholders back to your original code
                def restore_block(match):
                    idx = int(match.group(1))
                    if idx < len(blocks):
                        return blocks[idx]
                    return match.group(0)
                    
                # (?i) makes it case-insensitive just in case Google lowercases our placeholder
                res_restored = re.sub(r'(?i)\s*zxc(\d+)q\s*', restore_block, res)
                translated.append(res_restored)
                
        except Exception as e:
            print(f"    [!] Error: {e}")
            translated.append(p)

    return '\n\n'.join(translated)

files_to_process = []
for ext in ('**/*.md', '**/*.html'):
    files_to_process.extend(glob.glob(ext, recursive=True))

for filepath in files_to_process:
    filepath = filepath.replace('\\', '/')
    
    if filepath.startswith('cy/') or filepath.startswith('_site/') or 'README.md' in filepath:
        continue
        
    print(f"Translating safely: {filepath}...")
        
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