javascript:(function() {
    let p1 = document.getElementById("reflux-theme");
    let p2 = document.getElementById("reflux-display");
    
    if (p1 && p2) {
        var go = confirm("This theme is already running. Stop it?");
        if (go) {
            p1.remove();
            p2.remove();
            alert("This theme has been stopped.");
        } else {
            alert("This theme will continue running.");
        }
    } else {
        var go = confirm("Run this Reflux Theme?\n\nName: !name!\nAuthor: !author!\nDescription: !description!");
        if (go) {
            var style = document.createElement("style");
            var head = document.getElementsByTagName("head")[0];
            var target = document.getElementsByClassName("jsx-849184956")[0];
            
            style.setAttribute("id", "reflux-theme");
            style.appendChild(document.createTextNode(`!css!`));
            
            target.insertAdjacentHTML("afterend", `
            <a id="reflux-display" class="jsx-849184956" target="_blank" href="//reflux.repl.co/">
                <span class="jsx-849184956 sidebar-layout-nav-item-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 172 172" style="fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g fill="#00d1b2"><path d="M35.83333,21.5c-7.91917,0 -14.33333,6.41417 -14.33333,14.33333v100.33333c0,7.90483 6.4285,14.33333 14.33333,14.33333h100.33333c7.90483,0 14.33333,-6.4285 14.33333,-14.33333v-100.33333c0,-7.91917 -6.41417,-14.33333 -14.33333,-14.33333zM35.83333,35.83333h100.33333v14.33333h-100.33333zM35.83333,64.5h100.33333v71.66667h-100.33333zM71.66667,77.34961l-22.98372,22.98372l22.98372,22.98372l7.16667,-7.16667l-15.81706,-15.81706l15.81706,-15.81706zM100.33333,77.34961l-7.16667,7.16667l15.81706,15.81706l-15.81706,15.81706l7.16667,7.16667l22.98372,-22.98372z"></path></g></g>
                    </svg>
                </span>
                <div class="jsx-849184956">Reflux</div>
                <div class="jsx-849184956 beta-label">
                    <div style="background-color: #6262ff;" class="jsx-4210545632 beta-tag">ON</div>
                </div>
            </a>
            `);

            head.appendChild(style);
            alert("Reflux is now running!\n\nName: !name!\nAuthor: !author!");
        } else {
            alert("Reflux operation cancelled.");
        }
    }
})();