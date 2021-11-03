function reflux(referral) {
    if (referral == null || referral == "") {
        alert("Given referral code is empty or null.");
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

                alert(`Loaded '${data["name"]}' into Replit, enjoy!`);
            }
        })
        .catch(err => alert("Couldn't load theme.\n" + err))
    }
};

reflux("{{ referral }}");