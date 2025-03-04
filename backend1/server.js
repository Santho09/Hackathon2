const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(express.json());
app.use(cors());
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("✅ MongoDB Connected"))
    .catch(err => console.log("❌ MongoDB Connection Error:", err));


const dietRoutes = require("./routes/diet");  // Ensure the correct path
const workoutRoutes = require("./routes/workout");
const medicineRoutes = require("./routes/medicine");
const healthRoutes = require("./routes/health");
const sleepRoutes=require("./routes/sleep");



app.use("/api/diet", dietRoutes);
app.use("/api/workout", workoutRoutes);
app.use("/api/medicine", medicineRoutes);
app.use("/api/health", healthRoutes);
app.use("/api/sleep",sleepRoutes);
app.use((req, res, next) => {
    console.log(`➡ Received ${req.method} request for ${req.url}`);
    next();
});


const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
