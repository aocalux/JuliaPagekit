import re as re
import base64 as base64
from os.path import exists
from pathlib import Path


def hide_text(page_content):
    script = False

    if not exists(Path("docs/static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_02.JuliaPagekit-included.js")):
        with open("docs/static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_02.JuliaPagekit-included.js", "w") as emailsjs:
            emailsjs.write("""document.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll(".JuliaPagekit-included_02").forEach(element => {
            const text = element.dataset.juliapagekitincludeddata3;
    
            if (!text) return;
    
            element.textContent = new TextDecoder().decode(
                Uint8Array.from(atob(text), c => c.charCodeAt(0))
            );
        });
    });
            """.replace("\n", "") + "\n\n// from file: auto generated JavaScript file \n// This Page is using JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit")
            print("[JuliaPagekit] created static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_02.JuliaPagekit-included.js (text obfuscation)")

    text_pattern = r"\{JuliaPagekit\.ptext=([^{}]+)\}"

    def replace_text(match):
        nonlocal script

        text = match.group(1).strip()

        script_s = ""
        if not script:
            script_s = '<script src="/static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_02.JuliaPagekit-included.js" defer></script>'
            script = True

        return (
            f'<span class="JuliaPagekit-included_02" '
            f'data-juliapagekitincludeddata3="{base64.b64encode(text.encode("utf-8")).decode("utf-8")}"> '
            f'<i>[please activate JavaScript to view this content]</i>'
            f'</span>'
            f'{script_s}'
        )

    page_content = re.sub(text_pattern, replace_text, page_content)
    return page_content
