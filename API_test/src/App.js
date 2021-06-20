import { useState, useEffect } from "react";
import GetCourses from "./Api";

function App() {
  return (
    <div className="App">
      <button
        onClick={() =>
          GetCourses()
            .then((courseinfo) => {
              console.log(courseinfo);
            })
            .catch((err) => {
              console.log(err);
            })
        }
      >
        Get
      </button>
    </div>
  );
}

export default App;
