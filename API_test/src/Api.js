import axios from "axios";

const GetCourses = () => {
  return axios
    .get("https://mcmaster-course-api.herokuapp.com/courses/CLASSICS 1A03")
    .then((data) => {
      return data;
    })
    .catch((err) => {
      console.log(err);
    });
};

export default GetCourses;
