import axios from "axios";

const GetCourses = () => {
  // return axios
  //   .get("https://randomuser.me/api")
  //   .then(({ data }) => {
  //     console.log(data);
  //     return data;
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   });
  return axios
    .get("https://mcmaster-course-api.herokuapp.com/courses/CLASSICS 1A03")
    .then((data) => {
      console.log(data);
      return data;
    })
    .catch((err) => {
      console.log(err);
    });
};

export default GetCourses;
