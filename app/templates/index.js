var sel = document.getElementById("teams");
var img = document.querySelectorAll(".comparePlayers");

document.getElementById("btn").onclick = function() {
  var opts = sel.options;
  for (var j = 0; j != 3; j++) {
    if (opts[j].selected) {
      console.log(opts[j].text);
      team = opts[j].text;
      for (var i = 1; i <= 6; i++) {
        img[i - 1].src = "./players_img/kings" + team + i + ".png";
      }
    }
  }
};
