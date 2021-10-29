javascript:(function() {
    let p1 = document.getElementById("reflux-theme");
    let p2 = document.getElementById("reflux-display");
    
    if (p1 && p2) {
        var go = confirm("There is a Reflux theme already running. Would you like to stop it?");
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
            var target = document.getElementsByClassName("jsx-2607100739")[0];
            
            style.setAttribute("id", "reflux-theme");
            style.appendChild(document.createTextNode(`!css!`));

            if (target) {
                target.insertAdjacentHTML("afterend", 
                `
                <a id="reflux-display" class="jsx-2607100739" target="_blank" href="//github.com/frissyn/Reflux">
                    <span class="jsx-2607100739 sidebar-layout-nav-item-icon">
                    <img src="https://img.icons8.com/material-outlined/24/00D1B2/code.png"/>
                    </span>
                    <div class="jsx-2607100739">Reflux</div>
                    <div class="jsx-2607100739 beta-label">
                        <div style="background-color: #6262ff;" class="jsx-4210545632 beta-tag">ON</div>
                    </div>
                </a>
                `);
            } else {
                alert("Reflux badge could not be applied. This theme will run silently.");
            }

            head.appendChild(style);
            alert("Reflux is now running!");
        } else {
            alert("Reflux operation cancelled.");
        }
    }
})();
