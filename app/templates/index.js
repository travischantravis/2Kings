var sel = document.getElementById("teams");
var img = document.getElementById("comparePlayers");

document.getElementById("btn").onclick = function() {
  var opts = sel.options;
  for (var j = 0; j != 3; j++) {
    if (opts[j].selected) {
      console.log(opts[j].text);
      team = opts[j].text;
      img.src = "./players_img/kings" + team + ".png";
    }
  }
};
