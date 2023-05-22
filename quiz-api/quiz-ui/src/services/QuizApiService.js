import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true,
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
        return {
          status: error.response.status,
          data: error.response.data,
          message: error.message,
        };
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestByPosition(position) {
    return this.call("get", `questions?position=${position}`);
  },
  addParticipation(payload) {
    return this.call("post", "participations", payload);
  },
  getPassword(parameterPassword) {
    return this.call("post", "login", { password: parameterPassword });
  },
  getAllQuestion() {
    return this.call("get", "questions/all");
  },
  createQuestion(payload, token) {
    return this.call("post", "questions", payload, token);
  },
  updateQuestion(id, payload) {
    return this.call("put", `questions/${id}`, payload);
  },
  deleteQuestion(id, token) {
    console.log(token);
    return this.call("delete", `questions/${id}`, null, token);
  },
};
