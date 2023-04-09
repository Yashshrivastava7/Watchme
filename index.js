import express from "express";
const app = express();

const PORT = 8000;
app.get("/", (_, res) => {
  res.status(200).send("YOLO YOLO YOLO");
});

app.listen(PORT, () => {
  console.log(`Server running at port ${PORT}`);
});
