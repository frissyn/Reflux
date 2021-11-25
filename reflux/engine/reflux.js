(function reflux() {
    let referral = prompt("Enter a Reflux referral code.");

    if (referral == null || referral == "") {
        alert("Reflux theme injection cancelled.");
    } else {
        let URL = "https://api.reflux.repl.co/theme/";

        fetch(URL + referral)
        .then(res => res.json())
        .then(data => {
            let confirmed = confirm(
                `Name: ${data["name"]} \n` +
                `Author: ${data["author"]["name"]} \n` + 
                `Description: ${data["description"]} \n` +
                `Downloads: ${data["downloads"]}  \n\n` +
                `Load this theme?`
            );

            if (confirmed) {
                let target = document.getElementById("reflux-target");
                if (!target) {target = document.createElement("style")};

                target.type = "text/css";
                target.id = "reflux-target";
                target.textContent = data["stylesheet"];
                document.getElementsByTagName("head")[0].appendChild(target);

                setTimeout(function() {
                    monaco.editor.defineTheme("RefluxTheme", {
                        base: "vs-dark",
                        colors: {
                            "editor.background": data["monaco"],
                            "editor.selectionBackground": "#0f0fff",
                            "editorCursor.foreground": "#ffffff",
                        },
                        inherit: true,
                        rules: [
                            { token: "", foreground: "#ffffff" },
                        ]
                    });

                    store.subscribe(() => monaco.editor.setTheme("RefluxTheme"));
                }, 2000);

                /*
                MIT License

                Copyright (c) 2021 Brandon Lee, Connor Dennison, Piero Maddaleni, Scoder, Spidunno, and Coderma51

                Permission is hereby granted, free of charge, to any person obtaining a copy
                of this software and associated documentation files (the "Software"), to deal
                in the Software without restriction, including without limitation the rights
                to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
                copies of the Software, and to permit persons to whom the Software is
                furnished to do so, subject to the following conditions:

                The above copyright notice and this permission notice shall be included in all
                copies or substantial portions of the Software.

                THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
                IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
                FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
                AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
                LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
                OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
                SOFTWARE.
                */

                let topButtons = document.querySelectorAll('*[style="align-items: center; display: flex; justify-content: space-between;"]');
                topButtons[0].click();
                let canvasConsole = document.getElementsByClassName('xterm-text-layer')[0];
                topButtons[1].click();
                setTimeout(function(){
                    let canvasShell = document.getElementsByClassName('xterm-text-layer')[1];


                    topButtons[0].click();

                    let ctxConsole = canvasConsole.getContext("2d");
                    let ctxShell = canvasShell.getContext("2d");

                    ctxConsole.fillRectOriginal = ctxConsole.fillRect;
                    ctxShell.fillRectOriginal = ctxShell.fillRect;


                    ctxConsole.fillRect = function (...args) {
                        ctxConsole.fillStyle = data["xterm"];
                        ctxConsole.fillRectOriginal(...args)
                    }

                    ctxShell.fillRect = function (...args) {
                        ctxShell.fillStyle = data["xterm"];
                        ctxShell.fillRectOriginal(...args)
                    }

                }, 500)

                alert(`Loaded '${data["name"]}' into Replit, enjoy!`);
            }
        })
        .catch(err => alert("Couldn't load theme.\n" + err))
    }
})();