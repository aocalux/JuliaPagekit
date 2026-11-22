import re as re
import base64 as base64
from os.path import exists
from pathlib import Path


def hide_plaintext_mail(page_content):
    script = False

    if not exists(Path("docs/static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_01.JuliaPagekit-included.js")):

        with open("docs/static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_01.JuliaPagekit-included.js", "w") as emailsjs:
            emailsjs.write("""document.addEventListener("click", (event) => {
        const element = event.target.closest(".JuliaPagekit-included_01");
    
        if (!element) return;
        
        event.preventDefault();
        event.stopPropagation();
    
        const user = element.dataset.juliapagekitincludeddata1;
        const domain = element.dataset.juliapagekitincludeddata2;
    
        if (!user || !domain) return;
    
        const email = atob(user) + "@" + atob(domain);
    
        window.location.href = "mailto:" + email;
    });
    
    document.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll(".JuliaPagekit-included_01").forEach(element => {
            const user = element.dataset.juliapagekitincludeddata1;
            const domain = element.dataset.juliapagekitincludeddata2;
    
            if (!user || !domain) return;
    
            element.textContent = atob(user) + "@" + atob(domain);
            element.style.cursor = "pointer";
        });
    });
            """.replace("\n", "") + "\n\n// from file: auto generated JavaScript file \n// This Page is using JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit")
            print("[JuliaPagekit] created static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_01.JuliaPagekit-included.js (email obfuscation)")

    mail_pattern = r"\{JuliaPagekit\.email=([^{}]+)\}"

    def replace_mail(match):
        nonlocal script

        email = match.group(1).strip()

        if "@" not in email:
            return match.group(0)

        user, domain = email.split("@", 1)

        script_s = ""
        if not script:
            script_s = '<script src="/static/c2VociBzZWhyIGdlaGVpbWVyIFRleHQ_01.JuliaPagekit-included.js" defer></script>'
            script = True

        return (
            f'<a href="javascript:;" class="JuliaPagekit-included_01" '
            f'data-juliapagekitincludeddata1="{base64.b64encode(user.encode("ascii")).decode("ascii")}" '
            f'data-juliapagekitincludeddata2="{base64.b64encode(domain.encode("ascii")).decode("ascii")}">'
            f'<i>[please activate JavaScript to view this content]</i>'
            f'</a>'
            f'{script_s}'
        )

    page_content = re.sub(mail_pattern, replace_mail, page_content)
    return page_content
