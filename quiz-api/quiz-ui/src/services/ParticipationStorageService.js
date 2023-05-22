export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveToken(token) {
    window.localStorage.setItem("token", token);
  },
  getToken() {
    return window.localStorage.getItem("token");
  },
  saveParticipationScore() {
    window.localStorage.setItem("participationScore", JSON.stringify([]));
  },
  addToParticipationScore(item) {
    let participationScore = JSON.parse(
      window.localStorage.getItem("participationScore")
    );
    participationScore.push(item);
    window.localStorage.setItem(
      "participationScore",
      JSON.stringify(participationScore)
    );
  },
  getParticipationScore() {
    let participationScore = JSON.parse(
      window.localStorage.getItem("participationScore")
    );
    return participationScore.map((item) => parseInt(item));
  },
};
