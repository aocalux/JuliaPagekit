document.addEventListener("DOMContentLoaded", () => {    document.querySelectorAll(".JuliaPagekit-included_02").forEach(element => {        const text = element.dataset.juliapagekitincludeddata3;        if (!text) return;        element.textContent = new TextDecoder().decode(            Uint8Array.from(atob(text), c => c.charCodeAt(0))        );    });});        

// from file: auto generated JavaScript file 
// This Page is using JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit