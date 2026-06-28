import axios from "axios";

// backend URL (FastAPI)
const API = "http://127.0.0.1:8000";


// -------------------------
// UPLOAD FILE (PDF)
// -------------------------
export const uploadFile = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`${API}/upload`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};


// -------------------------
// ASK QUESTION (CHAT)
// -------------------------
export const askQuestion = (question) => {
  return axios.post(`${API}/ask`, {
    question: question,
  });
};