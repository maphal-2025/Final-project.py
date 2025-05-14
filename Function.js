import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [cropData, setCropData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/get_crop_data")
      .then(response => setCropData(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Crop Monitoring System</h1>
      <ul>
        {cropData.map((data, index) => (
          <li key={index}>Temp: {data.temp}, Humidity: {data.humidity}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;