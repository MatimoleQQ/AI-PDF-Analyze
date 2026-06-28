import { useState } from "react";
import { uploadFile } from "../api";

export default function UploadBox() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    await uploadFile(file);
    alert("PDF uploaded!");
  };

  return (
    <div>
      <h3>Upload PDF</h3>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload}>
        Upload
      </button>
    </div>
  );
}