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
  removePlayerName() {
    window.localStorage.removeItem("playerName");
  },
  saveToken(token) {
    window.localStorage.setItem("token", token);
  },
  getToken() {
    return window.localStorage.getItem("token");
  },
  removeToken() {
    window.localStorage.removeItem("token");
  },
  savePlayerScore(score) {
    window.localStorage.setItem("score", score);
  },
  getPlayerScore() {
    return window.localStorage.getItem("score");
  },
  removePlayerScore() {
    window.localStorage.removeItem("score");
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
