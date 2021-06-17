import React from "react";

const User = ({ img, name }) => {
  return (
    <div>
      {name}
      <img
        src={img}
        alt="user_image"
        style={{ paddingTop: "1rem", paddingLeft: "1rem" }}
      />
    </div>
  );
};

export default User;
