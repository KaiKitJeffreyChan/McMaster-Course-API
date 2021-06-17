import { useState, useEffect } from "react";
import GetCourses from "./Api";
import User from "./Components/user";

const getInfo = (userInformation) => {
  const {
    name: { first, last },
    picture: { large },
  } = userInformation;

  return { name: `Hello ${first} ${last}!!!`, img: large };
};

function App() {
  const [data, setData] = useState("");
  const [courses, setCourses] = useState("");
  const [userInformations, setUserInformations] = useState([]);

  // useEffect(() => {
  //   GetCourses()
  //     .then((retriveData) => {
  //       // setData(JSON.stringify(retriveData, null, 2));
  //       setUserInformations(retriveData.results);
  //       console.log(userInformations);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // }, []);

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
      {/* {userInformations.map((userInformation, idx) => {
        const { name, img } = getInfo(userInformation);
        return <User key="userInformation" name={name} img={img} />;
      })} */}
    </div>
  );
}

export default App;
